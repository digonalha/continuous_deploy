from app.configs import settings
from app.apis.telegram_api import send_document


def is_valid():
    return settings.chat_id and settings.api_token


def send_file(repo_name: str, log_path: str):
    if not is_valid():
        return

    message += (
        f"<b>Finalizando deploy da aplicação: {repo_name}</b>\n\n"
        f"<i>Essa mensagem está sendo enviada pela pipeline de deploy no dispositivo: {settings.computer_name}</i>"
    )

    send_document(message, log_path)
