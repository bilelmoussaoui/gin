FROM fedora:rawhide

RUN dnf update -y
# Required to build the spec files
RUN dnf install -y gcc dnf-plugins-core \
        rpm-build \
        rpm-devel rpmlint \
        make \
        python \
        bash \ 
        coreutils \
        diffutils \ 
        patch \
        rpmdevtools \
        git \
        gettext \ 
        python3-pip

# Bump meson version, we want to use the latest version as they might bring better cross build support
RUN pip3 install meson --upgrade 

# Required to build our bundle
RUN dnf install -y \
    mingw64-filesystem \
    mingw64-binutils \
    mingw64-gcc \
    mingw64-crt \
    mingw64-headers
