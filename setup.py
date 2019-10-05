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
