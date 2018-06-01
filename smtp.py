#!/usr/bin/python

import smtplib

sender = 'navratan1331@gmail.com'
receivers = ['ratanfor18@gmail.com']

message = """From: From Person <navratan1331@gmail.com>
To: To Person <ratanfor18@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
