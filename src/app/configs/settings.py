import os
from dotenv import load_dotenv

repository_path = ""
docker_compose_file_name = ""
computer_name = ""
sender_email = ""
receiver_email = ""
password = ""
api_token = ""
chat_id = ""


def is_valid():
    if not repository_path:
        raise Exception("cant find repository_path. check your .env file")
    elif not docker_compose_file_name:
        raise Exception("cant find docker_compose_file_name. check your .env file")


def load_variables():
    load_dotenv()

    # DEPLOY SETTINGS
    repository_path = os.getenv("REPOSITORY_DIR")
    docker_compose_file_name = os.getenv("FILENAME")
    computer_name = os.getenv("COMPUTERNAME")

    # EMAIL RESPONSE
    password = os.getenv("EMAIL_PASSWORD")
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")

    # TELEGRAM RESPONSE
    api_token = os.getenv("API_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    is_valid()
