"""
COMP.CS.100 ruutu syötetarkastuksella
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

def read_input(x: int):
    '''
    Calls an input field with given prompt. If the input is a positive integer, the input is returned.
    :param x: int, input prompt
    '''
    n = -1
    while True:
        n = int(input(x))
        if n > 0:
            return int(n)
        
def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
