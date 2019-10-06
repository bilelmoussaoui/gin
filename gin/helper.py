import shutil
import subprocess


def run_in_container(cmd):
    """
        Run the command in the pre-build docker container
    """
    supported_runners = ['podman', 'docker']
    command = []

    for runner in supported_runners:
        exec_path = shutil.which(runner)
        if exec_path:
            command.extend([
                exec_path,
                "-v", "",
                "docker.io/bilelmoussaoui/gin64",
            ])
            break
    if not exec_path:
        print("Couldn't find neither docker or podman, falling back to host")

    command.append(cmd)
    print(f"Running command: {''.join(command)}")
    subprocess.run(command)

