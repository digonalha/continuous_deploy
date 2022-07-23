# poc script p/ fazer deploy do projeto

from app.services import email_service, telegram_service, deploy_service
from app.configs import settings

settings.load_variables()

docker_compose_file_path = (
    f"{settings.repository_path}/{settings.docker_compose_file_name}"
)
log_path = f"{settings.repository_path}/deploy-output.log"


def main():
    update_result = deploy_service.deploy(
        settings.repository_path, log_path, docker_compose_file_path
    )

    if update_result:
        repository_name = deploy_service.get_repository_name(settings.repository_path)
        email_service.send_email(repository_name, log_path)
        telegram_service.send_file(repository_name, log_path)


if __name__ == "__main__":
    main()
