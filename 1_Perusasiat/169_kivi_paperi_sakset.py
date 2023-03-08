'''
COMP.CS.100 kivi paperi sakset
Tekijä: Oskari Heinonen
Opiskelijanumero: 151242115
'''

def main():
    choices = (input('Player 1, enter your choice (R/P/S): '),input('Player 2, enter your choice (R/P/S): '))
    if choices[0] == choices[1]:
        print("It's a tie!")
    elif (choices == ("R","S") or choices == ("P","R") or choices == ("S","P")):
        print('Player 1 won!')
    elif (choices == ("R","P") or choices == ("P","S") or choices == ("S","R")):
        print('Player 2 won!')

if __name__ == '__main__':
    main()