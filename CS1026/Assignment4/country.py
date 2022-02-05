# This class takes 4 parameters such as name, continent, population and area for countries.
# You can set countries parameters by using setter methods.
# Also this class print the result with using repr method.
class Country:
    def __init__(self, name, continent, pop, area):  # Init method takes 4 parameters.
        self.name = name  # country name
        self.pop = pop  # country population
        self.area = area  # country area
        self.continent = continent  # continent of country

    def getName(self):
        return self.name  # returns country name

    def getPop(self):
        return self.pop  # returns country population

    def getArea(self):
        return self.area  # returns country area

    def getContinent(self):
        return self.continent  # returns country's continent

    def setPop(self, other):  # setting country population with using other(new name) parameter.
        self.pop = other

    def setArea(self, other):  # setting country area with using other(new name) parameter.
        self.area = other

    def setContinent(self, other):  # setting country's continent with using other(new name) parameter.
        self.continent = other

    def __repr__(self):  # prints the below string by using name,pop,area,continent.
        return '{} (pop: {}, size: {}) in {}'.format(self.name, self.pop, self.area, self.continent)