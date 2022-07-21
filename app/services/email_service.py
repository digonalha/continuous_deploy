import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

sender_email = os.getenv("EMAIL_SENDER")
receiver_email = os.getenv("EMAIL_RECEIVER")
password = os.getenv("EMAIL_PASSWORD")


def is_valid():
    return sender_email and receiver_email and password


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
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    with open(log_dir) as f:
        body += f.read()

    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
