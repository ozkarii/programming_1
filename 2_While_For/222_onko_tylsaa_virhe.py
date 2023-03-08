'''
COMP.CS.100 tylsää virhe
Tekijä: Oskari Heinonen
'''

def main():
    answer = ""

    while answer != "Y" and answer != "N" and answer != "y" and answer != "n":
        answer = input('Answer Y or N: ')
        if answer != "Y" and answer != "N" and answer != "y" and answer != "n":
            print('Incorrect entry.')
    
    print('You answered ' + answer)

if __name__ == '__main__':
    main()