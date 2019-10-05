from .dependency import Dependency, DependencyType


class CMakeDependency(Dependency):
    _type = DependencyType.CMAKE

    def __init__(self, tag):
        Dependency.__init__(self, tag)
