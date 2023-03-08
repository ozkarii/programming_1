'''
COMP.CS.100 hymiöt
Tekijä: Oskari Heinonen
Opiskelijanumero: 151242115
'''

def main():
    mood = int(input('How do you feel? (1-10) '))
    if mood < 1 or mood > 10:
        print('Bad input!')
    elif mood == 10:
        print('A suitable smiley would be :-D')
    elif mood == 1:
        print("A suitable smiley would be :'(")
    elif mood > 7:
        print('A suitable smiley would be :-)')
    elif mood <= 7 and mood >= 4:
        print('A suitable smiley would be :-|')
    elif mood < 4:
        print('A suitable smiley would be :-(')
       

if __name__ == '__main__':
    main()