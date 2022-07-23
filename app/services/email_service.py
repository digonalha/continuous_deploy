import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.configs import settings


def is_valid():
    return settings.sender_email and settings.receiver_email and settings.password


def send_email(repo_name: str, log_dir: str):
    if not is_valid():
        return

    subject = "Finalizando deploy da aplicação: " + repo_name
    body = (
        "Esse email está sendo enviado pela pipeline de deploy no dispositivo: "
        + os.getenv("COMPUTERNAME")
        + "\n\n"
    )

    message = MIMEMultipart()
    message["From"] = settings.sender_email
    message["To"] = settings.receiver_email
    message["Subject"] = subject

    with open(log_dir) as f:
        body += f.read()

    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    # Login
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(settings.sender_email, settings.password)
        server.sendmail(settings.sender_email, settings.receiver_email, text)
