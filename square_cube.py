"""Autumn Capasso
UMUC SDEV 300
Cube and Square Lab
"""
import math
import sys


def square():
    """Lists for Square values"""
    square_list = set()
    for seed_value in range(1, 101):
        square_list.add(int(math.pow(seed_value, 2)))
    return set(square_list)


def cube():
    """List for for cube values"""
    cube_list = set()
    for seed_value in range(1, 101):
        cube_list.add(int(math.pow(seed_value, 3)))
    return set(cube_list)


def square_cube_union():
    print("Union of Cube and Square set:", cube_set.union(square_set))


def inter_of_sets():
    print("Intersection of the Cube and Square set:", cube_set.intersection(square_set))


def difference_of_sets():
    print("Difference of the Cube and Square Sets:",
          (cube_set.difference(square_set)),
          (square_set.difference(square_set)))


def search_int():
    int_input = int(input('Enter Interger that you would like the cube and square of: '))

    print(int_input, "=>", "\n, Square =", int_input, "^2 =", int_input * 2)
    print(int_input, "=>", "\n, Cube = ", int_input, "^3 =", int_input * 3)


# Exit Function
def end_program():
    """ Will end program """
    sys.exit()


# Creates the sets of integers, square set, and cube set
cube_set = cube()
square_set = square()


def main():
    """ Square and Cube Sets Lab """

    # Initialize Selection Value
    selection = -1
    # Square and Cube program
    while selection:
        # Display Menu
        print('Welcome to the Square and Cube Program')
        print('Main Menu')
        print('1.Display Square and Cube Values')
        print('2.Display the Union of Square and Cube sets')
        print('3. Display intersection of Square and Cube sets')
        print('4. Display Difference of Square and Cube sets ')
        print('5.Search for individual intergers')
        print('6.Quit Application')

        # Program takes in input
        print("Enter selection: ")
        selection = int(input())

    if selection == 1:
        print(sorted(square()))
        print(sorted(cube()))

    elif selection == 2:
        print(square_cube_union())

    elif selection == 3:
        print(inter_of_sets())

    elif selection == 4:
        print(difference_of_sets())

    elif selection == 5:
        print(search_int())

    elif selection == 6:
        end_program()

    else:
        print('Invalid entry')


if __name__ == "__main__":
    main()
