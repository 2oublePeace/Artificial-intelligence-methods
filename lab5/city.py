class City:

    def __init__(self, consumption, index=None):
        self.__consumption = consumption
        self.__index = index

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption):
        self.__consumption = consumption

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        self.__index = index
