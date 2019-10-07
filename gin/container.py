#
# Copyright (c) 2019 Bilal Elmoussaoui.
#
# This file is part of Gin
# (see https://github.com/bilelmoussaoui/gin).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
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
        return self._mingw_packages

    def run(self):
        # Before running the container, let's remove the image in case it's already exists
        subprocess.run(["docker", "rm", "gin", "-f"])

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

    def exec(self, command, **kwargs):
        _cmd = [self._runner, "exec", "-it", "gin"]
        _cmd.extend(command.split(" "))

        logger.info(f"Running command: {' '.join(_cmd)}")

        if kwargs.get("get_output"):
            output = subprocess.check_output(_cmd)
            return output.decode("utf-8")
        else:
            if kwargs.get("quiet"):
                subprocess.run(_cmd, stdout=subprocess.PIPE)
            else:
                subprocess.run(_cmd)

    def stop(self):
        subprocess.run([
            self._runner, "stop", "gin"
        ], stdout=subprocess.PIPE)

    def _start(self):
        subprocess.run([
            self._runner, "start", "gin"
        ], stdout=subprocess.PIPE)

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
