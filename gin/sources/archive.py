from .source import Source, SourceType


class ArchiveSource(Source):
    _type = SourceType.ARCHIVE

    url: str    # required: where the archive is
    sha256: str  # a hash to validate the archive

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.url = tag.get("url")
        self.sha256 = tag.get("sha256")
