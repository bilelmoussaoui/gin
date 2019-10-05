from .source import Source, SourceType


class ArchiveSource(Source):
    def __init__(self, tag):
        Source.__init__(self, tag)
        self._type = SourceType.ARCHIVE
