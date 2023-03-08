'''
COMP.CS.100 funktio listan alkioiden yhtäsuuruusvertailuun
Tekijä: Oskari Heinonen
'''

def are_all_members_same(l: list):
    '''
    Returns True if all items in the parameter list are equal.
    :param l: list, input list
    '''
    for i in l:
        if i != l[0]:
            return False
        else:
            pass
    return True

def main():
    print(are_all_members_same([]))

if __name__ == '__main__':
    main()