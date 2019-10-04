from gin.dependencies import Dependency


class Project:

    _id: str
    name: str
    manufacturer: str
    version: str
    dependencies: list[Dependency]
    module: Dependency
