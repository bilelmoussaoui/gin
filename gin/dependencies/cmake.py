from .dependency import Dependency, DependencyType


class CMakeDependency(Dependency):

    def __init__(self, tag):
        Dependency.__init__(self, tag)
        self._type = DependencyType.CMAKE
