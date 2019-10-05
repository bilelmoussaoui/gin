from .source import Source, SourceType


class ArchiveSource(Source):
    _type = SourceType.ARCHIVE

    def __init__(self, tag):
        Source.__init__(self, tag)
