from .dependency import Dependency, DependencyType


class AutotoolsDependency(Dependency):
    _type = DependencyType.AUTOTOOLS

    def __init__(self, tag):
        Dependency.__init__(self, tag)

    def get_flags(self):
        pass
