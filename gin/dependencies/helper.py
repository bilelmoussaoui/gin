
def find_dependencies(tree):
    from .dependency import Dependency, DependencyType

    supported_dependencies = DependencyType.all()
    dependencies = []

    for child in tree:
        if child.tag in supported_dependencies:
            dependencies.append(
                Dependency.new_with_type(child, child.tag)
            )
    return dependencies


def find_sources(tree):
    from gin.sources import Source, SourceType

    supported_sources = SourceType.all()
    sources = []

    for child in tree:
        if child.tag in supported_sources:
            sources.append(
                Source.new_with_type(child, child.tag)
            )
    return sources
