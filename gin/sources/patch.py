from .source import Source, SourceType


class PatchSource(Source):
    _type = SourceType.PATCH

    def __init__(self, tag):
        Source.__init__(self, tag)
