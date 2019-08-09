#this code is by : https://gist.github.com/nickoala/569a9d191d088d82a5ef5c03c0690a02
import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'bridgetorpy@gmail.com'
password = 'khorma12'
sender = 'bridgetorpy@gmail.com'
targets = ['bridges@torproject.org']

msg = MIMEText('get bridges')
msg['Subject'] = 'get bridges'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
