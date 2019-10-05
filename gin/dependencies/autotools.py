from .dependency import Dependency


class AutoToolsDependency(Dependency):

    def __init__(self, tag):
        Dependency.__init__(self, tag)
