#!/usr/bin/haserl
<%in p/common.cgi %>
<%
case "$POST_mode" in
  on)
    curl http://admin:${ui_password}@127.0.0.1/night/on
    ;;
  off)
    curl http://admin:${ui_password}@127.0.0.1/night/off
    ;;
  toggle)
    curl http://admin:${ui_password}@127.0.0.1/night/toggle
    ;;
  *)
    ;;
esac
header_ok
%>
