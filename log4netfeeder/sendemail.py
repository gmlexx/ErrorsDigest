# coding: utf-8
"""
This module can be started by crontab, 
when you'd like to receive error digest table as email.

crontab example:
0 10 * * * root cd /root/log4netfeeder/ && python sendemail.py admin1@company.com admin2@company.com
"""

import httplib, urllib
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

DIGEST_URL = "http://localhost/digest/"	# digest web root url
FEEDER_ADDR = "127.0.0.1" 		# log4netfeeder address
FEEDER_PORT = 8080			# log4netfeeder port
FROM_EMAIL = "digest@localhost"		#
SMTP_SERVER = "localhost"		#

conn = httplib.HTTPConnection(FEEDER_ADDR, FEEDER_PORT, timeout=30)
conn.request("GET", "/digest/")
res = conn.getresponse()
data = eval(res.read())
conn.close()

recipients = sys.argv

msg = MIMEMultipart('alternative')
msg['Subject'] = "Errors digest %s" % datetime.now().strftime("%Y-%m-%d %H:%M")
msg['From'] = FROM_EMAIL
msg['To'] = ", ".join(recipients)

html = u"""
<html>
<head>
<style type="text/css">
    body {font-family: arial,sans-serif; font-size: 10.5pt;}
    table {border: 1px solid black; border-collapse: collapse;}
    td {border: 1px solid black; padding:5px;}
</style>
</head>
<body>
<p><a href="%s">Errors digest</a></p>
<table><tr><td>Pattern</td><td>10 min</td><td>1 hour</td><td>4 hours</td><td>1 day</td><td>2 days</td></tr>
""" % DIGEST_URL
for item in data['digest']:
    has_errors = False
    row = u"<tr><td>" + item['name'] + "</td>"
    for count in item['counts']:
        if count['count'] > 0:
            has_errors = True
        row += "<td><a href=\"%s/pattern/%s/%s/\">%s</a></td>" % (DIGEST_URL.rstrip('/'), item['hash'], count['min'], count['count']) 
    row += "</tr>"
    if has_errors:
        html += row
html += """</table>
</body>
</html>"""

html_part = MIMEText(html, 'html', 'utf-8')
msg.attach(html_part)
s = smtplib.SMTP(SMTP_SERVER)
s.sendmail(FROM_EMAIL, recipients, msg.as_string())
s.quit()

