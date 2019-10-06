#!/bin/bash -e
NAME=docker.io/bilelmoussaoui/gin64

if [ -x "$(command -v docker)" ]; then
    docker build . -t "$NAME"
    docker push "$NAME"
else
    podman build . -t "$NAME"
    podman push "$NAME"
fi
