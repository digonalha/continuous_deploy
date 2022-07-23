import git as git_module
import subprocess
from datetime import datetime
from app.services import telegram_service
from app.configs import settings


def git_pull(repo_path: str) -> str:
    git = git_module.cmd.Git(repo_path)
    result_message = git.pull()

    return result_message


def get_repository_name(repo_path: str) -> str:
    repository = git_module.Repo(repo_path)
    repository_name = repository.remotes.origin.url.split(".git")[0].split("/")[-1]

    return repository_name


def deploy(
    repo_path: str,
    log_path: str,
    docker_compose_file_path: str,
    repository_name: str,
    pc_name: str,
) -> bool:
    result_message = git_pull(repo_path)

    if result_message != "Already up to date.":
        telegram_service.send_message(
            f"Iniciando deploy da aplicação <b>{repository_name}</b> no dispotivo <b>{pc_name}</b>..."
        )

        with open(log_path, "w") as output:
            output.write("\n")
            output.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            output.write(f"\n*********\n\n{result_message}\n\n")

            subprocess.call(
                f"docker-compose -f {docker_compose_file_path} up --build -d",
                shell=True,
                stdout=output,
                stderr=output,
            )

            subprocess.call(
                f'docker rmi $(docker images -f "dangling=true" -q)',
                shell=True,
                stdout=output,
                stderr=output,
            )

        return True

    return False
