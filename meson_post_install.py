#!/usr/bin/env python3
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

from os import environ, path
from subprocess import call

if not environ.get('DESTDIR', ''):
    PREFIX = environ.get('MESON_INSTALL_PREFIX', '/usr/local')
    DATA_DIR = path.join(PREFIX, 'share')
    print('Updating icon cache...')
    call(['gtk-update-icon-cache', '-qtf', path.join(DATA_DIR, 'icons/hicolor')])
    print("Updating mime info...")
    call(["update-mime-database", path.join(DATA_DIR, 'mime')])
