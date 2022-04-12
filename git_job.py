# poc github script to auto deploy project
from datetime import datetime
import os
import git as g
from git import Repo

import subprocess
import smtplib, ssl
from dotenv import load_dotenv

import smtplib, ssl
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

repo_dir = os.getenv("REPOSITORY_DIR")
file_name = os.getenv("FILENAME")
file_dir = f"{repo_dir}/{file_name}"
log_dir = f"{repo_dir}/deploy-output.log"


def run_job():
    git = g.cmd.Git(repo_dir)
    msg = git.pull()

    if msg != "Already up to date.":
        with open(log_dir, "w") as output:
            output.write("\n")
            output.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            output.write(f"\n*********\n\n{msg}\n\n")

            subprocess.call(
                f"docker-compose -f {file_dir} up --build -d",
                shell=True,
                stdout=output,
                stderr=output,
            )

            subprocess.call(
                f'docker rmi $(docker images -f "dangling=true" -q)',
                shell=True,
                stdout=output,
                stderr=output,
            )

        send_email()


def send_email():
    repo = Repo(repo_dir)
    repo_name = repo.remotes.origin.url.split(".git")[0].split("/")[-1]

    subject = "Finalizando deploy da aplicação: " + repo_name
    body = (
        "Esse email está sendo enviado pela pipeline de deploy no dispositivo: "
        + os.getenv("COMPUTERNAME")
        + "\n\n"
    )
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    with open(log_dir) as f:
        body += f.read()

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if __name__ == "__main__":
    run_job()
