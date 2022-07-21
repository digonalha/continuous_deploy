# poc script p/ fazer deploy do projeto
import os
from dotenv import load_dotenv
from app.services import email_service, telegram_service, deploy_service


load_dotenv()

repository_path = os.getenv("REPOSITORY_DIR")
docker_compose_file_name = os.getenv("FILENAME")
docker_compose_file_path = f"{repository_path}/{docker_compose_file_name}"
log_path = f"{repository_path}/deploy-output.log"


def main():
    update_result = deploy_service.deploy(
        repository_path, log_path, docker_compose_file_path
    )

    if update_result:
        repository_name = deploy_service.get_repository_name(repository_path)

        email_service.send_email(repository_name, log_path)
        if telegram_service.enabled():



if __name__ == "__main__":
    main()
