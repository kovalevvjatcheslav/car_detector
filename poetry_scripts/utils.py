import subprocess


def run_command(command: str):
    subprocess.run(command.split())


def up():
    command = "docker-compose -f docker/docker_compose.yml up --remove-orphans"
    run_command(command)


def down():
    command = "docker-compose -f docker/docker_compose.yml down"
    run_command(command)
