from .source import Source, SourceType
from gin.errors import MissingAttributeError


class GitSource(Source):
    _type = SourceType.GIT
    url: str 	# required: where the repo is
    commit: str  # a specific commit to use
    tag: str 	# the tag to use
    branch: str  # the branch to use

    def __init__(self, tag):
        Source.__init__(self, tag)
        self.url = tag.get("url")
        if not self.url:
            raise MissingAttributeError("Git source requires a url attribute")
        self.commit = tag.get("commit")
        self.branch = tag.get("branch")
        self.tag = tag.get("tag")

    def __str__(self):
        return self.url.rstrip(".git")
