"""
    Docker container helper utilitues
"""
import shutil
import subprocess

from logzero import logger

# The only contaienr we support.
CONTAINER_NAME = "docker.io/bilelmoussaoui/gin64"
    
def get_docker():
    """
        We can either run on a system with Docker or Podman in it.
        Let's us not hardcode docker everywhere.
    """
    supported_runners = ['podman', 'docker']

    for runner in supported_runners:
        exec_path = shutil.which(runner)
        if exec_path:
            return runner
            break
    if not exec_path:
        raise Exception("Couldn't find neither docker or podman, falling back to host")


class Container:
    _instance = None
    _id: str # Container ID
    _runner: str
    _workdir: str

    @staticmethod
    def get_default():
        if Container._instance is None:
            Container._instance = Container()
        return Container._instance

    def __init__(self, workdir):
        self._runner = get_docker()
        self._workdir = workdir
    
    def _start(self):
        subprocess.run([
            self._runner, "start", "gin"
        ])

    def run(self):
        container_id = subprocess.check_output([
            self._runner, "run", 
            "-it", "-d",
            "-v", f"{self._workdir}:/data:z",
            "-v", "/var/run/docker.sock:/var/run/docker.sock",
            "--name=gin",
            CONTAINER_NAME,
            "bash"
        ])
        self._id = container_id.decode("utf-8")
        logger.debug(f"Container is running: {self._id}")
        self._start()

    def exec(self, command):
        _cmd = [self._runner, "exec", "-it", "gin"]
        _cmd.extend(command.split(" "))

        subprocess.run(_cmd)
        logger.info(f"Running command: {' '.join(_cmd)}")

    def stop(self):
        subprocess.run([
            self._runner, "stop", "gin"
        ])
    
