#!/bin/bash -e
##
## Copyright (c) 2019 Bilal Elmoussaoui.
##
## This file is part of Gin 
## (see https://github.com/bilelmoussaoui/gin).
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##
NAME=docker.io/bilelmoussaoui/gin64

if [ -x "$(command -v docker)" ]; then
    docker build . -t "$NAME"
    docker push "$NAME"
else
    podman build . -t "$NAME"
    podman push "$NAME"
fi
