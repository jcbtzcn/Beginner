from catalogue import CountryCatalogue
# import CountryCatalogue class from catalogue
def processUpdates(cntryFileName, updateFileName):   #  Takes two files as parameters and updates country file.
    try:  # first it tries country file if it exists or not.
        country_file = open(cntryFileName, 'r')   # opens country file
        test1 = CountryCatalogue(country_file)
        country_file.close()
    except IOError:  #  To catch exceptions.
        x = input("The data file {} does not exist. Quit? Y/N: ".format(cntryFileName))  # Inputs user to quit or not.
        if not x == 'N':
            output = open('output.txt', 'w')  # writes update unsuccessful to output.txt file if file names are not correct.
            output.write("Update Unsuccessful\n")
            output.close()
            return False
        x = input("Enter a new file name: ")  # Asks user if they enters N to quit.
        return processUpdates(x, updateFileName)


    try:
        update_file = open(updateFileName, 'r')  # it opens the update file.
        update_list = []
        for line in update_file:
            line = line.strip()
            line = line.split(';')
            update_list.append(line)
        new_list = []
        for i in update_list:
            country = i[0]
            if len(i) == 1:    # for update country information with only one value(country name)
                c = ''
                p = ''
                a = ''
                new_list.append([country, c, p, a])
            if len(i) == 2:
                x = i[1].split('=')
                y = x[0]
                if 'C' in y:   # we are locating continent and adds it to list. ( if there is only country name and continent.)
                    p = ''
                    a = ''
                    new_list.append([country, x[1], p, a])
                elif 'A' in y:  # we are locating area and adds it to list.( if there is only country name and area.)
                    c = ''
                    p = ''
                    new_list.append([country, c, p, x[1]])
                elif 'P' in y:  # we are locating population and adds it to list. ( if there is only country name and population.)
                    a = ''
                    c = ''
                    new_list.append([country, c, x[1], a])
            if len(i) == 3:
                a = ''           # If a list line has 3 values, we will check which values do the lines have.
                p = ''           #  we are setting every possible combinations and by using if-elif conditions, we are
                c = ''           # adding them to list. If there is no information we use space.
                second = i[1].split('=')
                secondd = second[0]
                third = i[2].split('=')
                thirdd = third[0]
                if 'C' in secondd and 'P' in thirdd:
                    new_list.append([country, second[1], third[1], a])
                elif 'C' in secondd and 'A' in thirdd:
                    new_list.append([country, second[1], p, third[1]])
                elif 'P' in secondd and 'C' in thirdd:
                    new_list.append([country, third[1], second[1], a])
                elif 'P' in secondd and 'A' in thirdd:
                    new_list.append([country, c, second[1], third[1]])
                elif 'A' in secondd and 'P' in thirdd:
                    new_list.append([country, c, third[1], second[1]])
                elif 'A' in secondd and 'C' in thirdd:
                    new_list.append([country, third[1], p, third[1]])
                elif 'C' in secondd and 'C' in thirdd:
                    new_list.append([country, third[1], p, a])
                elif 'P' in secondd and 'P' in thirdd:
                    new_list.append([country, c, third[1], a])
                elif 'A' in secondd and 'A' in thirdd:
                    new_list.append([country, c, p, third[1]])
            if len(i) == 4:                       # If a list line has 4 values, we will check which values do the lines have.
                second_row = i[1].split('=')      #  we are setting every possible combinations and by using if-elif conditions
                second_roww = second_row[0]       # Since line length 4 means each updates in the list, we don't spaces.(empty strings)
                third_row = i[2].split('=')       #
                third_roww = third_row[0]
                fourth_row = i[3].split('=')
                fourth_roww = fourth_row[0]
                a = ''
                p = ''
                c = ''
                if 'C' in second_roww and 'P' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, second_row[1], third_row[1], fourth_row[1]])
                elif 'P' in second_roww and 'C' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, third_row[1], second_row[1], fourth_row[1]])
                elif 'P' in second_roww and 'A' in third_roww and 'C' in fourth_roww:
                    new_list.append([country, fourth_row[1], second_row[1], third_row[1]])
                elif 'C' in second_roww and 'A' in third_roww and 'P' in fourth_roww:
                    new_list.append([country, second_row[1], fourth_row[1], third_row[1]])
                elif 'A' in second_roww and 'C' in third_roww and 'P' in fourth_roww:
                    new_list.append([country, third_row[1], fourth_row[1], second_row[1]])
                elif 'A' in second_roww and 'P' in third_roww and 'C' in fourth_roww:
                    new_list.append([country, fourth_row[1], third_row[1], second_row[1]])
                elif 'C' in second_roww and 'C' in third_roww and 'C' in fourth_roww:  # if they are all continent update
                    new_list.append([country, fourth_row[1], p, c])
                elif 'P' in second_roww and 'P' in third_roww and 'P' in fourth_roww:
                    new_list.append([country, c, fourth_row[1], a])
                elif 'A' in second_roww and 'A' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, c, p, fourth_row[1]])
                elif 'C' in second_roww and 'C' in third_roww and 'P' in fourth_roww: # If two of them continent.
                    new_list.append([country, third_row[1], fourth_row[1], a])
                elif 'C' in second_roww and 'C' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, third_row[1], p, fourth_row[1]])
                elif 'A' in second_roww and 'C' in third_roww and 'C' in fourth_roww:
                    new_list.append([country, fourth_row[1], p, second_row[1]])
                elif 'P' in second_roww and 'C' in third_roww and 'C' in fourth_roww:
                    new_list.append([country, fourth_row[1], second_row[1], a])
                elif 'P' in second_roww and 'P' in third_roww and 'C' in fourth_roww: # if two of them population
                    new_list.append([country, fourth_row[1], third_row[1], a])
                elif 'P' in second_roww and 'P' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, c, third_row[1], fourth_row[1]])
                elif 'C' in second_roww and 'P' in third_roww and 'P' in fourth_roww:
                    new_list.append([country, second_row[1], fourth_row[1], a])
                elif 'A' in second_roww and 'P' in third_roww and 'P' in fourth_roww:
                    new_list.append([country, c, fourth_row[1], second_row[1]])
                elif 'A' in second_roww and 'A' in third_roww and 'C' in fourth_roww: # if two of them area
                    new_list.append([country, fourth_row[1], p, third_row[1]])
                elif 'A' in second_roww and 'A' in third_roww and 'P' in fourth_roww:
                    new_list.append([country, c, fourth_row[1], third_row[1]])
                elif 'C' in second_roww and 'A' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, second_row[1], p, fourth_row[1]])
                elif 'P' in second_roww and 'A' in third_roww and 'A' in fourth_roww:
                    new_list.append([country, c, second_row[1], fourth_row[1]])

        import string
        for key in new_list:
            country = string.capwords(key[0])  # we are using capswords for spaces, lower-upper key letters and capitalizing the words.
            continent_list = ['Antarctica', 'Arctic', 'Europe', 'Asia', 'Africa', 'North America',
                              'South America']
            continent_final = ''
            score = 0  # We set a score value to use at the end of this part.
            if key[1] != '':   # checking if continents values are valid.
                continent = string.capwords(key[1])
                if continent in continent_list:
                    continent_final = continent
                else:
                    score += 1
            else:
                continent_final = ''

            population_final = ''
            if key[2] != '':  #  population valid check.
                neww = string.capwords(key[2])
                new = neww.split(',')
                population = ''
                tot = 0
                for line in new[1:]:
                    if len(line) == 3:
                        population = population + ',' + line
                    elif len(line) != 3:
                        tot += 1

                if tot == 0 and 1 <= len(new[0]) <= 3:
                    firstnumber = new[0]
                    population_final = firstnumber + population
                else:
                    score += 1
            else:
                population_final = ''

            area_final = ''
            if key[3] != '':  #  area valid check
                neww = string.capwords(key[3])
                new = neww.split(',')
                area = ''
                tot = 0
                for line in new[1:]:
                    if len(line) == 3:
                        area = area + ',' + line
                    elif len(line) != 3:
                        tot += 1

                if tot == 0 and 1 <= len(new[0]) <= 3:
                    firstnumber = new[0]
                    area_final = firstnumber + area
                else:
                    score += 1
            else:
                area_final = ''

            if score == 0:
                test1.addCountry(country, continent_final, population_final, area_final)
            else:
                print('Invalid value.')

        for key in new_list:
            country = string.capwords(key[0])# to use setPopulation method.
            if key[2] != '':
                neww = string.capwords(key[2])
                new = neww.split(',')
                total = ''
                tot = 0
                for line in new[1:]:
                    if len(line) == 3:
                        total = total + ',' + line
                    elif len(line)!= 3:
                        tot += 1

                if tot == 0 and 1<= len(new[0])<=3:
                     firstnumber = new[0]
                     total2 = firstnumber + total
                     test1.setPopulationOfCountry(country, total2)
                else:
                    print('Explanation:Not a valid population value for population of {}.'.format(key[0]))  # prints if values are invalid.
        for key in new_list:
            country = string.capwords(key[0])  # to use setArea method.
            if key[3] != '':
                neww = string.capwords(key[3])
                new = neww.split(',')
                total = ''
                tot = 0
                for line in new[1:]:
                    if len(line) == 3:
                        total = total + ',' + line
                    elif len(line) != 3:
                        tot += 1

                if tot == 0 and 1 <= len(new[0]) <= 3:
                    firstnumber = new[0]
                    total2 = firstnumber + total
                    test1.setAreaOfCountry(country, total2)
                else:
                    print('Explanation:Not a valid area value for area of {}.'.format(key[0])) # prints if values are invalid.

        for key in new_list: # to use setcontinent method.
            result2 = string.capwords(key[0])
            if key[1] != '':
                word = key[1].lower()
                word2 = string.capwords(word)
                continent_list = ['Antarctica', 'Arctic', 'Europe', 'Asia', 'Africa', 'North America',
                                  'South America']
                if word2 in continent_list:
                    test1.setContinentOfCountry(result2, word2)
                else:
                    print('Explanation:Not a valid continent value for continent of {}.'.format(key[0]))  # prints if values are invalid.
        test1.updated_list()
        test1.saveCountryCatalogue('output.txt')
        return True


    except IOError:  #  tries to open update file and if it is not a valid name then it return an exception.
        y = input("The update file {} does not exist. Quit? Y/N: ".format(updateFileName)) # Asks users if they wanna quit or not.
        if not y == 'N':
            output = open('output.txt', 'w')  # Writes an empty string with update unsuccessful.
            output.write("Update Unsuccessful\n")
            output.close()
            return False
        y = input("Enter a new file name: ") # it asks user a new file name for update file.
        return processUpdates(cntryFileName, y)