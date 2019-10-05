from .dependency import Dependency


class MesonDependency(Dependency):

    def __init__(self, tag):
        Dependency.__init__(self, tag)
