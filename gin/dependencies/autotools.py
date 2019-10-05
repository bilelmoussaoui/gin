from .dependency import Dependency, DependencyType


class AutoToolsDependency(Dependency):

    def __init__(self, tag):
        Dependency.__init__(self, tag)
        self._type = DependencyType.AUTOTOOLS
