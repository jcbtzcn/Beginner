# This program is coded to calculate the volume of cube,pyramid and ellipsoid.
# Enter q or quit to quit program. You can quit without prompting nothing.
# Prompted shapes will be printed in order with two decimal points.
from volume import volume_of_cube, volume_of_ellipsoid, volume_of_pyramid
# Imports value from volume.py file to provide volumes of shapes.
user_input = input('Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ')  # Prompt the user for shape.
user_input = user_input.lower().strip()  # Accept all lower and upper cases and including spaces between characters.
wordList = user_input.split()
user_input = ' '.join(wordList)
volumes_list = []
if user_input not in ('q', 'quit'):  # User can quit without entering nothing.
    while user_input not in ('q', 'quit'):  # Prompts the user until q or Quit entered.
        if user_input in ('cube', 'c', 'pyramid', 'p', 'ellipsoid', 'e', 'quit', 'q'):
            if user_input not in ('q', 'quit'):  # It provides not to ask anything after q or Quit entered.
                if user_input in ('cube', 'c'):
                    length_side_input = float(input('Enter the length side for the cube: '))
                    volCube = volume_of_cube(length_side_input)
                    print('The volume of cube with side %.2f is:  %.2f' % (length_side_input, volCube))
                    volCube = '%.2f' % volCube
                    volumes_list.append(('cube', volCube))  # Appends cube tuple to list.
                if user_input in ('pyramid', 'p'):
                    base_length_pyramid = float(input('Enter the base of the pyramid: '))
                    height_pyramid = float(input('Enter the height of the pyramid: '))
                    volPyramid = volume_of_pyramid(base_length_pyramid, height_pyramid)
                    print('The volume of a pyramid with base %.2f and height %.2f is:  '
                          '%.2f' % (base_length_pyramid, height_pyramid, volPyramid))
                    volPyramid = '%.2f' % volPyramid
                    volumes_list.append(('pyramid', volPyramid))  # Appends pyramid tuple to list.
                if user_input in ('ellipsoid', 'e'):
                    first_radius = float(input('Enter the first radius: '))
                    second_radius = float(input('Enter the second radius: '))
                    third_radius = float(input('Enter the third radius: '))
                    volEllipsoid = volume_of_ellipsoid(first_radius, second_radius, third_radius)
                    print('The volume of an ellipsoid with radius %.2f and %.2f and %.2f is :  '
                          '%.2f' % (first_radius, second_radius, third_radius, volEllipsoid))
                    volEllipsoid = '%.2f' % volEllipsoid
                    volumes_list.append(('ellipsoid', volEllipsoid))  # Appends ellipsoid tuple to list.
        else:
            print('Invalid Input. Please enter a valid choice (quit/q, cube/c, pyramid/p, ellipsoid/e): ')
        user_input = input('\nPlease enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ')
        user_input = user_input.lower().strip()  # Accepts lower or upper case quit versions after first prompts.
        wordList = user_input.split()
        user_input = ' '.join(wordList)
    print('Output: Volume of shapes entered in sorted order: ')
    volumes_list.sort(key=lambda volumes_list: float(volumes_list[1]))  # Organizes the list in order.
    for i in range(len(volumes_list)):    # Places every tuple in different line as sorted above.
        print(volumes_list[i][0], volumes_list[i][1])
else:
    print('Output: No shapes entered.')