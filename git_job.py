# test github script to auto deploy project
from datetime import datetime
import os
import git as g
import subprocess
from dotenv import load_dotenv

load_dotenv()

repo_dir = os.getenv("REPOSITORY_DIR")
file_name = os.getenv("FILENAME")
file_dir = f"{repo_dir}/{file_name}"

git = g.cmd.Git(repo_dir)
msg = git.pull()

print(msg)

with open(f"{repo_dir}/deploy-output.log", "w") as output:
    output.write("\n")
    output.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    output.write(f"\n*********\n\n{msg}\n\n")

    if msg != "Already up to date.":
        subprocess.call(
            f"docker-compose -f {file_dir} up --build -d",
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
