from .dependency import Dependency, DependencyType


class MesonDependency(Dependency):
    _type = DependencyType.MESON

    def __init__(self, tag):
        Dependency.__init__(self, tag)

    def get_flags(self):
        flags = ""
        for key, val in self._flags.items():
            flags += f"-D{key}={val}"
        return flags
