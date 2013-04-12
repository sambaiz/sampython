# -*- coding: utf-8 -*-
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send(from_addr, to_addr, msg):
    s = smtplib.SMTP()
    s.connect()
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.close()

if __name__ == '__main__':
    from_addr = 'spam@example.com'
    to_addr = 'sambaiz@sambla.net'
    msg = create_message(from_addr, to_addr, 'good morning', 'おはよう！')
    send(from_addr, to_addr, msg)

