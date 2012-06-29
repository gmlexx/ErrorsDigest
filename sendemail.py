# coding: utf-8
import httplib, urllib
import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8080

conn = httplib.HTTPConnection(BACKEND_HOST, BACKEND_PORT, timeout=30)
conn.request("GET", "/")
res = conn.getresponse()
data = res.read()
conn.close()

me = "dd-health-monitor@localhost"
recipients = sys.argv[1:]

msg = MIMEMultipart('alternative')
msg['Subject'] = "Errors digest %s" % datetime.now().strftime("%Y-%m-%d %H:%M")
msg['From'] = me
msg['To'] = ", ".join(recipients)

html_part = MIMEText(data, 'html', 'utf-8')
msg.attach(html_part)
s = smtplib.SMTP('mail.host')
s.sendmail(me, recipients, msg.as_string())
s.quit()
