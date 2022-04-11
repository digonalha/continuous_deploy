# test github script to auto deploy project
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

if msg != "Already up to date.":
    with open(f"{repo_dir}/deploy-output.log", "w") as output:
        subprocess.call(
            f"docker-compose.exe -f {file_dir} up --build -d",
            shell=True,
            stdout=output,
            stderr=output,
        )
