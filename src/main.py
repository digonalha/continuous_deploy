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
        )

        if update_result:
            message = (
                f"O deploy da aplicação <b>{repository_name}</b> foi finalizado!\n\n"
                f"🎉🎉🎉"
            )
            telegram_service.send_file(message, log_path)
    except Exception as ex:
        telegram_service.send_message(
            f"Ocorreu um erro ao tentar fazer o deploy da aplicação <b>{repository_name}</b>\n\n"
            f"💀💀💀\n\n"
            f"Erro: {ex}"
        )
        raise


if __name__ == "__main__":
    main()
