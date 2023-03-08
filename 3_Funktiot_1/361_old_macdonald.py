'''
COMP.CS.100 old macdonald had a farm
Tekijä: Oskari Heinonen
'''

def print_verse(animal: str, sound: str) -> str:
    '''
    Prints the song Old MacDonald Had a Farm with user specified animals and their corresponding sounds.
    :param animal: str, specified animal
    :param sound: str, sound of the animal
    '''
    print('Old MACDONALD had a farm')
    print('E-I-E-I-O')
    print('And on his farm he had a ' + str(animal))
    print('E-I-E-I-O')
    print('With a', str(sound), str(sound), 'here')
    print('And a', str(sound), str(sound), 'there')
    print('Here a', str(sound) + ',', 'there a', str(sound))
    print('Everywhere a', str(sound), str(sound))
    print('Old MacDonald had a farm')
    print('E-I-E-I-O')


def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")

if __name__ == '__main__':
    main()