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
import logging
import os

import jinja2
import logzero

ENVIRONMENT = "prod"
CONTAINER_NAME = "docker.io/bilelmoussaoui/gin64"
IMAGE_NAME = "gin"

# Templates
dir_path = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(dir_path, 'templates')

loader = jinja2.FileSystemLoader(template_dir)

template_env = jinja2.Environment(loader=loader)
template_env.trim_blocks = True
template_env.lstrip_blocks = True

# Logging
if ENVIRONMENT == "dev":
    level = logging.INFO
else:
    level = logging.ERROR


log_format = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
formatter = logzero.LogFormatter(fmt=log_format)
logger = logzero.setup_logger(name="gin", level=level, formatter=formatter)
