import requests
from app.configs import settings


def send_document(message: str, log_path: str, parse_mode: str = "HTML"):
    data = {
        "chat_id": settings.chat_id,
        "caption": message,
        "parse_mode": parse_mode,
    }

    files = {
        "document": open(log_path, "rb"),
    }

    api_uri = f"https://api.telegram.org/bot{settings.api_token}"

    res = requests.post(f"{api_uri}/sendDocument", data=data, files=files)
    print(res)
