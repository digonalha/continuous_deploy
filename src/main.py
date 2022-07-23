# poc script p/ fazer deploy do projeto
from app.configs import settings
from app.services import telegram_service, deploy_service

docker_compose_file_path = (
    f"{settings.repository_path}/{settings.docker_compose_file_name}"
)
log_path = f"{settings.repository_path}/deploy-output.log"


def main():
    try:
        repository_name = deploy_service.get_repository_name(settings.repository_path)

        update_result = deploy_service.deploy(
            settings.repository_path,
            log_path,
            docker_compose_file_path,
            repository_name,
            settings.device_name,
        )

        if update_result:
            message = (
                f"<b>Finalizando deploy da aplicação: {repository_name}</b>\n\n"
                f"<i>Essa mensagem está sendo enviada pela pipeline de deploy no dispositivo <b>{settings.device_name}<b></i>"
            )
            telegram_service.send_file(message, log_path)
    except Exception as ex:
        telegram_service.send_message(
            f"<b>Um erro ocorreu ao tentar fazer o deploy da aplicação: {repository_name}</b>\n\nErro: {ex}"
        )
        raise


if __name__ == "__main__":
    main()
