from .source import Source, SourceType
from gin.errors import MissingAttributeError


class PatchSource(Source):
    _type = SourceType.PATCH
    path: str  # the patch file to apply

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.path = tag.get("path")
        if self.path is None:
            raise MissingAttributeError("Patch tag requires path attribute")
