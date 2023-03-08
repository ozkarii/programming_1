'''
COMP.CS.100 paranneltu ruudun tulostus
Tekijä: Oskari Heinonen
'''

def print_box(width: int, height: int, border_mark='#', inner_mark=' '):
    '''
    Prints a box with given parameters.
    :param width: int, box width
    :param height: int, box height
    :param border_mark: str, a string the box edges are drawn with
    :param inner_mark: str, a string the box's inside is drawn with
    '''
    print(border_mark * width)
    i = 1
    while i <= height - 2:
        print(border_mark + inner_mark * (width - 2) + border_mark)
        i += 1
    print(border_mark * width)


def main():
    print_box(5, 4)
    print()
    print_box(3, 8, "*")
    print()
    print_box(5, 4, "O", "o")
    print()
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == '__main__':
    main()