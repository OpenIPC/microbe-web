#!/bin/sh

plugin="email"
config_file="/etc/webui/${plugin}.conf"
curl_timeout=100

log_file=/tmp/webui/${plugin}.log
mkdir -p $(dirname $log_file)
:>$log_file

show_help() {
  echo "Usage: $0 [-f address] [-t address] [-s subject] [-b body] [-h]
  -f address  Sender's email address
  -t address  Recipeint's email address
  -s subject  Subject line.
  -b body     Letter body.
  -h          Show this help.
"
  exit 0
}

# read variables from config
[ -f "$config_file" ] && source $config_file

# override config values with command line arguments
while getopts f:t:s:b:h flag; do
  case ${flag} in
  b) email_body=${OPTARG} ;;
  f) email_from_address=${OPTARG} ;;
  s) email_subject=${OPTARG} ;;
  t) email_to_address=${OPTARG} ;;
  h) show_help ;;
  esac
done

[ "false" = "$email_enabled" ] &&
  echo "Sending to email is disabled." && exit 10

# validate mandatory values
[ -z "$email_smtp_host" ] &&
  echo "SMTP host not found in config" && exit 11
[ -z "$email_smtp_port" ] &&
  echo "SMTP port not found in config" && exit 12
[ -z "$email_from_address" ] &&
  echo "Sender's email address not found" && exit 13
[ -z "$email_to_address" ] &&
  echo "Recipient's email address not found" && exit 14

# assign default values if not set
#[ -z "$email_from_name" ] && email_from_name="OpenIPC Camera"
#[ -z "$email_to_name"   ] && email_to_name="OpenIPC Camera Admin"
#[ -z "$email_subject"   ] && email_subject="Snapshot from OpenIPC Camera"

command="curl --verbose --silent" # --insecure
command="${command} --connect-timeout ${curl_timeout}"
command="${command} --max-time ${curl_timeout}"

if [ "true" = "$email_smtp_use_ssl" ]; then
  command="${command} --ssl --url smtps://"
else
  command="${command} --url smtp://"
fi
command="${command}${email_smtp_host}:${email_smtp_port}"

command="${command} --mail-from ${email_from_address}"
command="${command} --mail-rcpt ${email_to_address}"
command="${command} --user '${email_smtp_login}:${email_smtp_password}'"

if [ "$#" -eq 0 ]; then
  snapshot="/tmp/${plugin}_snap.jpg"
  curl "http://127.0.0.1/image.jpg?t=$(date +"%s")" --output "$snapshot" --silent
  [ $? -ne 0 ] && echo "Cannot get a snapshot" && exit 2

  email_body="$(date -R)"
  command="${command} -H 'Subject: ${email_subject}'"
  command="${command} -H 'From: "${email_from_name}" <${email_from_address}>'"
  command="${command} -H 'To: "${email_to_name}" <${email_to_address}>'"
  command="${command} -F '=(;type=multipart/mixed'"
  command="${command} -F '=${email_body};type=text/plain'"
  command="${command} -F 'file=@${snapshot};type=image/jpeg;encoder=base64'"
  command="${command} -F '=)'"
else
  email_file="/tmp/email.$$.txt"
  {
    echo "From: ${email_from_name} <${email_from_address}>"
    echo "To: ${email_to_name} <${email_to_address}>"
    echo "Subject: ${email_subject}"
    echo "Date: $(date -R)"
    echo ""
    echo "${email_body}"
  } >>$email_file
  command="${command} --upload-file ${email_file}"
fi

echo "$command" >>$log_file
eval "$command" >>$log_file 2>&1
cat $log_file

[ -f ${snapshot} ] && rm -f ${snapshot}
[ -f ${email_file} ] && rm -f ${email_file}

exit 0
