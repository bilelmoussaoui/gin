from .source import Source, SourceType


class PatchSource(Source):
    _type = SourceType.PATCH
    path: str  # the patch file to apply

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.patch = tag.get("path")
