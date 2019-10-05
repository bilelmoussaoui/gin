from .source import Source, SourceType
from gin.errors import MissingAttributeError


class ArchiveSource(Source):
    _type = SourceType.ARCHIVE

    url: str    # required: where the archive is
    sha256: str  # a hash to validate the archive

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.url = tag.get("url")
        if not self.url:
            raise MissingAttributeError(
                "Archive source requires a url attribute")
        self.sha256 = tag.get("sha-256")
        if not self.sha256:
            raise MissingAttributeError(
                "Archive source requires a sha256 attribute")
