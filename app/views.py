from django.shortcuts import render
import smtplib, ssl
from django.http import HttpResponse
# Create your views here.


def index(request):

    return render(request,'index.html')


def sendMessage(request):

    email = request.POST.get("email")
    subject = request.POST.get("subject")
    msg = request.POST.get("message")
    # print(email)
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "ankitshantikunj@gmail.com"
    password = input("Type your password and press enter: ")
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, "ankitshantikunj@gmail.com", message)

    return render(request,'index.html') 