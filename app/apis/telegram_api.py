import requests
from app.configs import settings

API_URI = f"https://api.telegram.org/bot{settings.api_token}"


def send_document(message: str, log_path: str, parse_mode: str = "HTML"):
    document = open(log_path, "rb")

    data = {
        "chat_id": settings.chat_id,
        "text": message,
        "parse_mode": parse_mode,
        "document": document,
    }

    res = requests.post(f"{API_URI}/sendDocument", data=data)
    print(res)
