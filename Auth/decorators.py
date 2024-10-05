from django.http import HttpResponse
from django.shortcuts import redirect,render
from email.message import EmailMessage
import random
# def allowed_users(allowed_roles)
otp=""
for i in range(7):
    a=str(random.randint(0,9))
    otp+=a

import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('aajbookotp@gmail.com',"lpyy ddeb yyae nhde")


msg=EmailMessage()
msg['Subject']="AAJBook.com OTP Verification"
msg["From"]="aajbookotp@gmail.com"
msg["To"]="jai.agarwal622@gmail.com"
msg.set_content(f"Your Otp is :{otp}")
server.send_message(msg)
print("EmailSent")