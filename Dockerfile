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
RUN echo -e "[options]\nCacheDir=/data/pacman/cache/\n[ownstuff]\nSigLevel = Optional TrustAll\nServer = https://martchus.no-ip.biz/repo/arch/\$repo/os/\$arch\nServer = https://ftp.f3l.de/~martchus/\$repo/os/\$arch\n$(cat /etc/pacman.conf)" > /etc/pacman.conf

RUN pacman -Sy --noconfirm --needed base base-devel binutils unzip wget filesystem bash pacman sudo fakeroot git bzr svn meson cmake
RUN pacman -Syu --noconfirm

RUN pacman -S --noconfirm mingw-w64-gcc

RUN wget -P /usr/bin https://raw.githubusercontent.com/msys2/MSYS2-packages/master/pacman/makepkg-mingw && chmod +x /usr/bin/makepkg-mingw
RUN wget -P /etc https://raw.githubusercontent.com/msys2/MSYS2-packages/master/pacman/makepkg_mingw64.conf
