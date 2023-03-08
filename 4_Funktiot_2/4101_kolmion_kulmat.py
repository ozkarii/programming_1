'''
COMP.CS.100 
Tekijä: Oskari Heinonen
'''

def calculate_angle(angle_1: int,angle_2=90):
    '''
    Returns the value of the third angle when the values of first and second angles are given.
    :param angle_1: int, first angle
    :param angle_2: int, second angle
    '''
    return 180 - angle_1 - angle_2


def main():
    print(calculate_angle(50,60))

if __name__ == '__main__':
    main()