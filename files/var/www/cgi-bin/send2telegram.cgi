#!/usr/bin/haserl
<%in p/common.cgi %>
<%
/usr/sbin/send2telegram.sh >/dev/null
redirect_back
%>
