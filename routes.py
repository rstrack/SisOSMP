class Routes():
    def __init__(self) -> None:
        self.routes = dict()

    def setRoute(self, flag:str, obj:object):
        self.routes[flag] = obj

    def getRoute(self, flag:str):
        return self.routes[flag]


handleRoutes = Routes()
