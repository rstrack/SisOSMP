class Container():
    def __init__(self) -> None:
        self.container = dict()

    def setDep(self, flag:str, obj:object):
        self.container[flag] = obj

    def getDep(self, flag:str):
        return self.container[flag]

handleDeps = Container()

