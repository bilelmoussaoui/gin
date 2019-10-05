from .source import Source, SourceType


class GitSource(Source):
    _type = SourceType.GIT

    def __init__(self, tag):
        Source.__init__(self, tag)
