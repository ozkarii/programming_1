'''
COMP.CS.100 
Tekijä: Oskari Heinonen
'''

def is_the_list_in_order(l: list):
    '''
    Returns True if the paramer list is sorted in ascending order.
    :param l: list, list to be checked
    '''
    l_sorted = l.copy()
    l_sorted.sort()
    if l == l_sorted:
        return True
    else:
        return False

def main():
    return

if __name__ == '__main__':
    main()