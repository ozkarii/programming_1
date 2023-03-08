"""
COMP.CS.100 geometriset kuviot
Tekijä: Oskari Heinonen
"""

from math import pi

def square(l: float):
    '''
    Returns the circumference and surface area of a square with given side lenght.
    :param l: float, lenght of square's side
    '''
    circ = rounder(4 * l)
    area = rounder(l ** 2)
    return circ, area

def rectangle(l1: float,l2: float):
    '''
    Returns the circumference and surface area of a rectangle with given side lenghts.
    :param l1: float, lenght of rectangle's side 1
    :param l2: float, lenght of rectangle's side 2
    '''
    circ = rounder(2 * l1 + 2 * l2)
    area = rounder(l1 * l2)
    return circ, area

def circle(r: float):
    '''
    Returns the circumference and surface area of a circle with given radius.
    :param r: float, lenght of circle's radius
    '''
    circ = rounder(2 * pi * r)
    area = rounder(pi * r ** 2)
    return circ, area

def check_input(input_prompt: str):
    '''
    Asks user input until input is positive. Then returns input.
    :param input_prompt: str, input prompt used
    '''
    while True:
        n = float(input(input_prompt))
        if n > 0:
            return n

def print_results(circ: float,area: float):
    '''
    Prints the reuslts of the calculations.
    :param circ: float, circumference to be printed
    :param area: float, surface area to be printed
    '''
    print("The circumference is",str(circ))
    print("The surface area is",str(area))

def rounder(n: float):
    '''
    Formats the calculation result to 2 decimals.
    :param n: number to be formatted
    '''
    return f"{n:.2f}"


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")
        
        if answer == "s":
            lenght = check_input("Enter the length of the square's side: ")
            circ, area = square(lenght)
            print_results(circ,area)

        elif answer == "r":
            lenght_1 = check_input("Enter the length of the rectangle's side 1: ")
            lenght_2 = check_input("Enter the length of the rectangle's side 2: ")
            circ, area = rectangle(lenght_1,lenght_2)
            print_results(circ,area)
        
        elif answer == "c":
            radius = check_input("Enter the circle's radius: ")
            circ, area = circle(radius)
            print_results(circ,area)

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
