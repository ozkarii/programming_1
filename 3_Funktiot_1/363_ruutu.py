"""
COMP.CS.100 ruudun tulostaminen
Tekijä: Oskari Heinonen
"""

def print_box(width: int, height: int, mark: str):
    '''
    Prints a box with given parameters.
    :param width: int, box width
    :param height: int, box height
    :param mark: str, a string the box is drawn with
    '''
    i = 1
    while i <= int(height):
        print(mark*int(width))
        i += 1


def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
