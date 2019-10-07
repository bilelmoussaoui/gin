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
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gin",
    version="0.1",
    author="Bilal Elmoussaoui",
    author_email="bil.elmoussaoui@gmail.com",
    description="Not Wine",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license='MIT',
    include_package_data=True,
    url="https://github.com/bilelmoussaoui/gin",
    entry_points={
        'console_scripts': ['gin=gin.cli:run'],
    },
    packages=[
        'gin',
        'gin.dependencies',
        'gin.export',
        'gin.sources',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Topic :: Utilities',
    ],
    test_suite='tests'
)
