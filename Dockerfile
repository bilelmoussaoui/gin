FROM fedora:31

RUN dnf update -y
RUN dnf install -y \
    mingw64-filesystem \
    mingw64-binutils \
    mingw64-gcc \
    mingw64-crt \
    mingw64-headers
