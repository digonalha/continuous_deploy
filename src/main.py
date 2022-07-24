# poc script p/ fazer deploy do projeto
from app.configs import settings
from app.services import telegram_service, deploy_service

docker_compose_file_path = (
    f"{settings.repository_path}/{settings.docker_compose_file_name}"
)

repository_name = deploy_service.get_repository_name(settings.repository_path)
log_path = f"{settings.repository_path}/deploy-output.log"


def main():
    try:

        update_result = deploy_service.deploy(
            settings.repository_path, log_path, docker_compose_file_path
        )

        if update_result:
            message = f"O deploy da aplicação <b>{repository_name}</b> no dispositivo <b>{settings.device_name}</b> foi finalizado 🎉🎉🎉"
            telegram_service.send_file(message, log_path)
    except Exception as ex:
        telegram_service.send_message(
            f"Ocorreu um erro ao tentar fazer o deploy da aplicação <b>{repository_name}</b> no dispositivo <b>{settings.device_name}</b> 💀💀💀"
        )
        raise


main()
