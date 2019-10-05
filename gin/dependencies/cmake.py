from .dependency import Dependency


class CMakeDependency(Dependency):

    def __init__(self, tag):
        Dependency.__init__(self, tag)
