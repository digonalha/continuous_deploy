from app.configs import settings
from app.apis import telegram_api


def is_valid():
    return settings.chat_id and settings.api_token


def send_file(caption: str, file_path: str):
    if not is_valid():
        return

    caption += f"\n\n<i>Essa mensagem está sendo enviada pela pipeline de deploy no dispositivo <b>{settings.device_name.upper()}</b></i>"

    telegram_api.send_document(caption, file_path)


def send_message(message: str):
    if not is_valid():
        return

    message += f"\n\n\n<i>Essa mensagem está sendo enviada pela pipeline de deploy no dispositivo <b>{settings.device_name.upper()}</b></i>"

    telegram_api.send_message(message)
