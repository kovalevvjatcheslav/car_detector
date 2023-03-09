import subprocess


def run_command(command: str):
    subprocess.run(command.split())


def up():
    command = "docker-compose -f docker/docker_compose.yml up --remove-orphans"
    run_command(command)


def down():
    command = "docker-compose -f docker/docker_compose.yml down"
    run_command(command)


def build_images():
    commands = [
        "docker build -f docker/image_processor.docker -t image_processor .",
        "docker build -f docker/detector.docker -t detector .",
    ]
    for command in commands:
        run_command(command)


def migrate():
    commands = [
        "docker-compose -f docker/docker_compose.yml exec image_processor alembic upgrade head",
    ]
    for command in commands:
        run_command(command)


def tests():
    commands = [
        "pytest -s",
    ]
    for command in commands:
        run_command(command)
