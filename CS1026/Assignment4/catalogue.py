from country import Country  # import Country class from country file.
# This class takes a country data file as parameter.
# There 3 setter methods for continent, population and area of the countries.
# There is findCountry method which uses country object.
# There is  addCountry method for new country updates.
# There is printCatalogue method which prints the updated list.
# Finally, updatedFile and SaveCatalogue methods return updated lists and write them to a file and check if updating
# is successful.
class CountryCatalogue:
    def __init__(self, countryFile):  # takes country file as parameter and processes it.
        self.countryCat = []   # creates a list.
        self.countryFile = countryFile
        for line in self.countryFile:
            line = str(line).split('|')
            row = line[3].replace('\n', '')  # removes the new line.
            self.countryCat.append([line[0], line[1], line[2], row])  # creates a list by using the file.


    def setPopulationOfCountry(self, countryName, newPop):
        for line in self.countryCat[1:]:
            if countryName in line[0]:
                line[2] = newPop     # updates the population of country


    def setAreaOfCountry(self, countryName, newArea):
        for line in self.countryCat[1:]:
            if countryName in line[0]:
                line[3] = newArea    # updates the area of country

    def setContinentOfCountry(self, countryName, newCont):
        for line in self.countryCat[1:]:
            if countryName in line[0]:
                line[1] = newCont    # updates the continent of country


    def findCountry(self, country):    # finds the country object if it exists in country catalogue.
        score = 0
        for line in self.countryCat:
            if country.getName() in line:
                score += 1

        if score == 1:
            return country
        else:
            return None

    def addCountry(self, countryName, cont, pop, area):    # adds new country to list.
        count = 0

        for line in self.countryCat[1:]:   # to pass the header, we use [1:]
            if countryName in line[0]:
                count += 1
        if count == 0:
            self.countryCat.append([countryName, cont, pop, area])

    def printCountryCatalogue(self):  # prints the updated list by using country repr method.
        my_list = []
        self.countryCat[:1] = my_list
        self.countryCat.sort()
        for line in self.countryCat:    # prints the rest of the list.
            test2 = Country(line[0], line[1], line[2], line[3])
            print(test2.__repr__())

    def updated_list(self):   # writes the list to an output file by creating.
        file = open('output.txt', 'w')
        for line in range(len(self.countryCat)):
            if line <= len(self.countryCat)-2:  # eliminates the last new line
                file.write('{}|{}|{}|{}\n'.format(self.countryCat[line][0], self.countryCat[line][1]
                                                  , self.countryCat[line][2], self.countryCat[line][3]))
            else:  # eliminates the last new line
                file.write('{}|{}|{}|{}'.format(self.countryCat[line][0], self.countryCat[line][1],
                                                  self.countryCat[line][2], self.countryCat[line][3]))


    def saveCountryCatalogue(self, fname):  # takes updated fname as parameter.
        file = open('cataloguefile.txt', 'w')  # creates a new file to write the list.
        file_name = open(fname, 'r')
        for line in range(len(self.countryCat)):
            if line <= len(self.countryCat)-2:
                file.write('{}|{}|{}|{}\n'.format(self.countryCat[line][0], self.countryCat[line][1]
                                                  , self.countryCat[line][2], self.countryCat[line][3]))
            else:
                file.write('{}|{}|{}|{}'.format(self.countryCat[line][0], self.countryCat[line][1],
                                                  self.countryCat[line][2], self.countryCat[line][3]))
        file = open('cataloguefile.txt', 'r')
        file_name = file_name.read()
        file = file.read()
        if file_name == file:  # compares two files to check if the updating was successful.
              return '{}|{}|{}|{}'.format(self.countryCat[0][0], self.countryCat[0][1],
                                       self.countryCat[0][2], self.countryCat[0][3])
        if file_name == file:
              my_list = []
              self.countryCat[:1] = my_list
              self.countryCat.sort()   # sorts the list except the header.
              for line in self.countryCat:
                  print('{}|{}|{}|{}'.format(line[0], line[1], line[2], line[3]))
        else:
            print('-1')   # returns -1 if the updating is not successful.

