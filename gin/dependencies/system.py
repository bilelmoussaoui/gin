from .dependency import Dependency


class SystemDependency(Dependency):

    def __init__(self, tag):
        Dependency.__init__(self, tag)
