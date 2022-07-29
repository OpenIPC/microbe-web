#!/bin/sh

plugin="ftp"
config_file="/etc/webui/${plugin}.conf"
curl_timeout=100

log_file=/tmp/webui/${plugin}.log
mkdir -p $(dirname $log_file)
:>$log_file

show_help() {
  echo "Usage: $0 [-h host] [-p port] [-u username] [-P password] [-d path] [-f file] [-h]
  -s host     FTP server FQDN or IP address.
  -p port     FTP server port.
  -d path     Directory on server, relative to FTP root.
  -f file     File to upload.
  -u username FTP username.
  -P password FTP password.
  -h          Show this help.
"
  exit 0
}

# read variables from config
[ -f "$config_file" ] && source $config_file

# override config values with command line arguments
while getopts d:f:p:P:s:u:h flag; do
  case ${flag} in
  d) ftp_path=${OPTARG} ;;
  f) ftp_file=${OPTARG} ;;
  p) ftp_port=${OPTARG} ;;
  P) ftp_password=${OPTARG} ;;
  s) ftp_host=${OPTARG} ;;
  u) ftp_username=${OPTARG} ;;
  h) show_help ;;
  esac
done

[ "false" = "$ftp_enabled" ] &&
  echo "Sending to FTP is disabled." && exit 10

# validate mandatory values
[ -z "$ftp_host" ] &&
  echo "FTP host not found" && exit 11
[ -z "$ftp_port" ] &&
  echo "FTP port not found" && exit 12

if [ -z "$ftp_file" ]; then
  snapshot="/tmp/${plugin}_snap.jpg"
  curl "http://127.0.0.1/image.jpg?t=$(date +"%s")" --output "$snapshot" --silent
  [ $? -ne 0 ] && echo "Cannot get a snapshot" && exit 2
  ftp_file=$snapshot
fi

command="curl --verbose --silent" # --insecure
command="${command} --connect-timeout ${curl_timeout}"
command="${command} --max-time ${curl_timeout}"

# SOCK5 proxy, if needed
if [ "true" = "$ftp_socks5_enabled" ]; then
  source /etc/webui/socks5.conf
  command="${command} --socks5-hostname ${socks5_host}:${socks5_port}"
  command="${command} --proxy-user ${socks5_login}:${socks5_password}"
fi

command="${command} --url ftp://"
[ -n "$ftp_username" ] && [ -n "$ftp_password" ] &&
  command="${command}${ftp_username}:${ftp_password}"
command="${command}@${ftp_host}"
[ -n "$ftp_path" ] &&
  command="${command}/${ftp_path// /%20}"
command="${command}/$(date +"$ftp_template")"
command="${command} --upload-file ${ftp_file}"
command="${command} --ftp-create-dirs"

echo "$command" >>$log_file
eval "$command" >>$log_file 2>&1
cat $log_file

[ -f ${snapshot} ] && rm -f ${snapshot}

exit 0
