FROM archlinux/base


RUN pacman --noconfirm -Sy
# Create user
RUN useradd -m -g wheel -s /bin/sh tester
RUN echo "tester ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN mkdir /data
RUN chown -R tester:wheel /data
RUN chgrp -R wheel /data
RUN chmod -R g+w /data

# FIXME: add msys pgp key instead of disabling signature validation
# RUN pacman -S --noconfirm awk
# RUN pacman-key --init
# RUN pacman-key --populate archlinux
# RUN pacman-key --recv-keys "AD351C50AE085775EB59333B5F92EFC1A47D45A1"

# RUN echo -e "\n[msys]\nServer = http://repo.msys2.org/msys/x86_64/\nSigLevel = Never\n$(cat /etc/pacman.conf)" > /etc/pacman.conf


# Set Cache directory
RUN echo -e "[options]\nCacheDir=/data/pacman/cache/\n$(cat /etc/pacman.conf)" > /etc/pacman.conf
# Enable multilib (for wine)
RUN echo -e "[multilib]\nInclude = /etc/pacman.d/mirrorlist\n$(cat /etc/pacman.conf)" > /etc/pacman.conf
# Enable a third party repo to get few pre-built mingw-w64 packages 
RUN echo -e "[ownstuff]\nSigLevel = Optional TrustAll\nServer = https://martchus.no-ip.biz/repo/arch/\$repo/os/\$arch\nServer = https://ftp.f3l.de/~martchus/\$repo/os/\$arch\n$(cat /etc/pacman.conf)" > /etc/pacman.conf

# Update the system
RUN pacman -Syu --noconfirm

# Install packaging tools
RUN pacman -Sy --noconfirm --needed base-devel \
                                    binutils \
                                    unzip \
                                    wget \
                                    filesystem \
                                    bash \
                                    pacman \
                                    sudo \
                                    fakeroot \
                                    git \
                                    bzr \
                                    svn \
                                    meson \
                                    cmake
# Install mingw-64 build stuff 
RUN pacman -S --noconfirm mingw-w64-gcc

# Install Wine
RUN pacman -S wine winetricks --noconfirm
RUN su - tester -c "wine wineboot --init && winetricks --unattended dotnet40 dotnet_verifier"