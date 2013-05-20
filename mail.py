# -*- coding: utf-8 -*-
import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from twitter import Twitter

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
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
    lines = data.split('\n')
    return lines

if __name__ == '__main__':
    from_addr = 'spam@example.com'
    twitter = Twitter()
    lines = address_read('maillist.txt')
    for line in lines:
        if line == '': break
        print line
        msg = create_message(from_addr, line, 'ツイートがあります', twitter.random_select(100).encode('utf8'))
        send(from_addr, line, msg)
