'''
COMP.CS.100 
Tekijä: Oskari Heinonen
'''

def compare_floats(x1: float,x2: float,EPSILON: float) -> bool:
    '''
    Returns True if the two given floats are equal within the specified accuracy of EPSILON.
    :param x1: float, number 1
    :param x2: float, number 2
    '''
    if abs(x1 - x2) < EPSILON:
        return True
    else:
        return False

def main():
    return    

if __name__ == '__main__':
    main()