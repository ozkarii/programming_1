'''
COMP.CS.100 
Tekijä: Oskari Heinonen
'''

def create_an_acronym(words: str):
    '''
    Returns an acronymm of the string.
    :paramas word: str, word to make an acronym out of
    '''
    words = words.split()
    acronym = []
    for i in words:
        acronym.append(i[0])
    acronym = ''.join(acronym).upper()
    return acronym


def main():
    print(create_an_acronym('acs basda casa'))

if __name__ == '__main__':
    main()