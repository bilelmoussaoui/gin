from .dependency import Dependency, DependencyType

from gin.errors import ParseError


class SystemDependency(Dependency):

    def __init__(self, tag):
        self._type = DependencyType.SYSTEM
        Dependency.__init__(self, tag)

    def get_flags(self):
        raise ParseError("System dependencies don't support flags")
