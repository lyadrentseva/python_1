# -*- coding: utf-8 -*-

# auto send e-mails
import smtplib
import mimetypes
import email
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()               # объект обработки почтовых вложений
FROM = "*************@gmail.com"    # ящик, с которого высылается письмо
TO = "**********@gmail.com"       # ящик, на который высылается письмо
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = 'time to say hello '
text = "hello everybody!!"

part = MIMEText(text, 'plain', 'utf-8')
msg.attach(part)
attachment = MIMEBase('application', "octet-stream")

with open(r"/home/red/PycharmProjects/python_belhard/social.jpg", "rb") as f:
    data = f.read()
    attachment.set_payload(data)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename="social.jpg")
    msg.attach(attachment)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)     # порт и номер порта
server.login("*********a@gmail.com", "********")  # адрес почты и пароль от ящика почты
server.sendmail(FROM, TO, msg.as_string())
server.quit()

## how to us lib requests

import requests #библиотека для создания запросов в url

url = 'https://news.tut.by/culture/592436.html'

r = requests.get(url)

text = r.text #получить всё содержимое html-страницы со всем форматированием

# js = r.json() 


import re

s = re.findall(r'<head>\w*', text)


u = 'https://wex.nz/api/3/ticker/btc_usd-btc_rur'
r = requests.get(u)
js = r.json() 
js['btc_usd']['avg']

z = requests.get('https://wex.nz/api/3/ticker/btc_usd-btc_rur').json()['btc_usd']['avg']


y = lambda: requests.get('https://wex.nz/api/3/ticker/btc_usd-btc_rur').json()['btc_usd']['avg']

requests.get('https://wex.nz/api/3/ticker/btc_usd-btc_rur').json() 

