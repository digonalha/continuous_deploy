import os
from dotenv import load_dotenv

repository_path = ""
docker_compose_file_name = ""
device_name = ""
api_token = ""
chat_id = ""


def is_valid():
    if not repository_path:
        raise Exception("cant find repository_path. check your .env file")
    elif not docker_compose_file_name:
        raise Exception("cant find docker_compose_file_name. check your .env file")
    elif not device_name:
        raise Exception("cant find device_name. check your .env file")


def load_variables():
    load_dotenv()
    global repository_path, docker_compose_file_name, device_name, api_token, chat_id

    # DEPLOY SETTINGS
    repository_path = os.getenv("REPOSITORY_DIR")
    docker_compose_file_name = os.getenv("FILENAME")
    device_name = os.getenv("DEVICE_NAME")

    # TELEGRAM RESPONSE
    api_token = os.getenv("API_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    is_valid()


load_variables()
