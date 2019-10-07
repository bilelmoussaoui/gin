"""
    Docker container helper utilitues
"""
import shutil
import subprocess
import re

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
        raise Exception(
            "Couldn't find neither docker or podman, falling back to host")


class Container:
    _instance = None
    _id: str  # Container ID
    _runner: str
    _workdir: str
    _mingw_packages: []

    @staticmethod
    def get_default():
        if Container._instance is None:
            Container._instance = Container()
        return Container._instance

    def __init__(self, workdir):
        self._runner = get_docker()
        self._workdir = workdir
        self.run()
        self._fetch_mingw_packages()

    def get_mingw_packages(self):
        print(self._mingw_packages)
        return self._mingw_packages

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

    def exec(self, command, get_output=False):
        _cmd = [self._runner, "exec", "-it", "gin"]
        _cmd.extend(command.split(" "))

        logger.info(f"Running command: {' '.join(_cmd)}")

        if get_output:
            output = subprocess.check_output(_cmd)
            return output.decode("utf-8")
        else:
            subprocess.run(_cmd)

    def stop(self):
        subprocess.run([
            self._runner, "stop", "gin"
        ])

    def _start(self):
        subprocess.run([
            self._runner, "start", "gin"
        ])

    def _fetch_mingw_packages(self):
        """
            We need to fetch the list of mingw64 packages
            As each system dependency might not be available as a mingw64 package
            For now we fallback to the default packages, it might cause breakage later.
        """
        self.exec("dnf update")
        packages_output = self.exec("dnf search mingw64", get_output=True)
        # Remove ansi charachters
        # From https://stackoverflow.com/a/45448194
        ansi_regex = r'\x1b(' \
            r'(\[\??\d+[hl])|' \
            r'([=<>a-kzNM78])|' \
            r'([\(\)][a-b0-2])|' \
            r'(\[\d{0,2}[ma-dgkjqi])|' \
            r'(\[\d+;\d+[hfy]?)|' \
            r'(\[;?[hf])|' \
            r'(#[3-68])|' \
            r'([01356]n)|' \
            r'(O[mlnp-z]?)|' \
            r'(/Z)|' \
            r'(\d+)|' \
            r'(\[\?\d;\d0c)|' \
            r'(\d;\dR))'
        ansi_escape = re.compile(ansi_regex, flags=re.IGNORECASE)
        packages_output = ansi_escape.sub('', packages_output)
        packages = []
        for package in packages_output.split("\n"):
            if package.startswith("mingw64-"):
                packages.append(package.split(
                    ".")[0].strip().replace("mingw64-", ""))
        self._mingw_packages = packages
