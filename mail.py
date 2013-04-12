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

def address_read(filename):
    f = open(filename)
    data = f.read()
    f.close()
    lines = data.split('\\n')
    return lines

if __name__ == '__main__':
    from_addr = 'spam@example.com'
    lines = address_read('maillist.txt')
    for line in lines:
        msg = create_message(from_addr, line, 'good morning', 'おはよう！')
        send(from_addr, line, msg)

