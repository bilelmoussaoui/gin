from .source import Source, SourceType


class DirSource(Source):
    _type = SourceType.DIR

    def __init__(self, tag):
        Source.__init__(self, tag)
