'''
COMP.CS.100 arvosanojen korvaus
Tekijä: Oskari Heinonen
'''

def convert_grades(grades: list):
    '''
    Alters list's values so that all values greater than zero are changed to 6.
    :param grades: list, list to be altered
    '''
    c = 0
    for i in grades:
        if i > 0:
            grades[c] = 6
            c += 1
        else:
            c += 1


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
