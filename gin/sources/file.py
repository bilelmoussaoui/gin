from .source import Source, SourceType


class FileSource(Source):
    _type = SourceType.FILE

    def __init__(self, tag):
        Source.__init__(self, tag)
