'''
COMP.CS.100 yogi bear laulu
Tekijä: Oskari Heinonen
'''

def repeat_name(name: str, reps: int):
    '''
    Returns the given name, given amount of times.

    :param name: str, name of the character for the verse
    :param reps: int, amount of times the name should be returned
    '''
    if reps == 1:
        s = name + ', ' + name
        return s
    elif reps == 3:
        # Pitäisi olla NoneType, ei str
        s = name + ', ' + name + ' Bear' + "\n" + name + ', ' + name + ' Bear' + "\n" + name + ', ' + name + ' Bear'
        return s

def verse(lyric: str, name: str):
    '''
    Prints the verse with specified lyrics.

    :param lyrics: str, lyrics for the verse
    :param name: str, name of the character for the verse
    '''
    print(lyric)
    print(repeat_name(name,1))
    print(lyric)
    print(repeat_name(name,3))
    print(lyric)
    print(repeat_name(name,1),"Bear")



def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == '__main__':
    main()


#I know someone you don't know
# Yogi, Yogi
# I know someone you don't know
# Yogi, Yogi Bear
# Yogi, Yogi Bear
# Yogi, Yogi Bear
# I know someone you don't know
# Yogi, Yogi Bear
