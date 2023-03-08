'''
COMP.CS.100 tylsää 2
Tekijä: Oskari Heinonen
'''

def main():
    state = ''
    while state != 'y' and state != 'Y':
        state = input('Bored? (y/n) ') 
        while state != 'n' and state != 'N' and state != 'y' and state != 'Y':
            print('Incorrect entry.')
            state = input('Bored? (y/n) ')
    print("Well, let's stop this, then.")

if __name__ == '__main__':
    main()