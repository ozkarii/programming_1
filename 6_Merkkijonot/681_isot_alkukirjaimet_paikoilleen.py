'''
COMP.CS.100 
Tekijä: Oskari Heinonen
'''

def capitalize_initial_letters(words: str):
    '''
    Trasnsforms the initial of all words in a string into uppercase and the rest to lowercase.
    :param words: str, a single string of words separated with " "
    '''
    words = words.split()
    i = 0
    while i < len(words):
        words[i] = words[i].capitalize()
        i += 1
    return ' '.join(words)


def main():
    print(capitalize_initial_letters("lol xD xx fafasFF"))

if __name__ == '__main__':
    main()