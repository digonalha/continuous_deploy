import requests
from app.configs import settings

API_URI = "https://api.telegram.org/bot" + settings.api_token


def send_document(message: str, log_path: str, parse_mode: str = "HTML"):
    data = {
        "chat_id": settings.chat_id,
        "caption": message,
        "parse_mode": parse_mode,
    }

    files = {
        "document": open(log_path, "rb"),
    }

    requests.post(f"{API_URI}/sendDocument", data=data, files=files)


def send_message(message: str, parse_mode: str = "HTML"):
    data = {
        "chat_id": settings.chat_id,
        "text": message,
        "parse_mode": parse_mode,
    }

    res = requests.post(f"{API_URI}/sendMessage", data=data)
    print(res)
