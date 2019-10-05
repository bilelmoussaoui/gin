
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
