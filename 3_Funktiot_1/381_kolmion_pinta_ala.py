"""
COMP.CS.100 kolmion pinta-ala
Tekijä: Oskari Heinonen
"""

from math import sqrt

def area(a: float,b: float,c: float):
    '''
    Returns the area of a triangle given the lenghts of the sides
    :param a: float, lenght of side 1
    :param b: float, lenght of side 2
    :param c: float, lenght of side 3
    '''

    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    return A

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    print("The triangle's area is " + str(round(area(a,b,c),1)))


if __name__ == "__main__":
    main()
