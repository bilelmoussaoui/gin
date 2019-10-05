from .source import Source, SourceType


class DirSource(Source):
    def __init__(self, tag):
        Source.__init__(self, tag)
        self._type = SourceType.DIR
