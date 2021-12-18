class Factory:

    def __init__(self, production, index=None):
        self.__production = production
        self.__index = index
        self.__items = None

    @property
    def production(self):
        return self.__production

    @production.setter
    def production(self, production):
        self.__production = production

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        self.__index = index

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = items
