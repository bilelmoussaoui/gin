from abc import ABCMeta, abstractmethod

class BuildSystemType:
    CMAKE = "cmake"
    MESON = "meson"


class BuildSystem(metaclass=ABCMeta):
    flags: list[(str, str)]


    @abstractmethod
    def add_flag(self, name, value):
        return

    @abstractmethod
    def prepare(self):
        return


    @abstractmethod
    def install(self, files: list[str]):
        return