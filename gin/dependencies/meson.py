from .dependency import Dependency, DependencyType


class MesonDependency(Dependency):
    _type = DependencyType.MESON

    def __init__(self, tag):
        Dependency.__init__(self, tag)
