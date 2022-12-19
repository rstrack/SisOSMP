class Container:
    def __init__(self) -> None:
        self.container = {}

    def setDep(self, flag: str, obj: object):
        self.container[flag] = obj

    def getDep(self, flag: str):
        return self.container[flag]


handle_deps = Container()
