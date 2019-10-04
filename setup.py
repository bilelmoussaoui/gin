import setuptools
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)


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
    url="https://github.com/bilelmoussaoui/gin",
    packages=[
        'gin',
        'gin.dependencies',
        'gin.export',
        'gin.sources'
    ],
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
    ],
    tests_require=test_requirements,
    test_suite='tests'
)
