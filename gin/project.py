
from gin.dependencies import Dependency


class Project:

    _id: str
    name: str
    manufacturer: str
    version: str
    module: Dependency

    def __init__(self, **kwargs):
        self._id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.manufacturer = kwargs.get("manufacturer")
        self.version = kwargs.get("version")
        self.module = kwargs.get("module")

    def get_id(self):
        return self._id
