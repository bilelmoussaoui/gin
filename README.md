# Gin
![Python Build](https://github.com/bilelmoussaoui/gin/workflows/Python%20package/badge.svg) [![codecov](https://codecov.io/gh/bilelmoussaoui/gin/branch/master/graph/badge.svg)](https://codecov.io/gh/bilelmoussaoui/gin)


![logo](logo.png)

Gin is a Windows Installer creator.


## 📦 Build
- Install `pipenv`
- Install the dependencies `pipenv install --ignore-pipfile`
- Run `gin --help`

## 🛠 Scripts
Ensure you have installed Gin using `pipenv install --ignore-pipfile --dev` for development dependencies

- Tests: `pipenv run tests`
- Build: `pipenv run build`
- Install: `pipenv run install`
- Flake8: `pipenv run flake8`
- Autopep8: `pipenv run lint`


### How to use
- Pull the docker image
```
docker pull docker.io/bilelmoussaoui/gin64
```

- Install Gin into a new virtual environnement
```
pipenv run install
pipenv shell
```

```
gin init tests/org.gnome.design.Palette.gin.xml
```
