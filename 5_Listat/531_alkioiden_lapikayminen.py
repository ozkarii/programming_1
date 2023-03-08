'''
COMP.CS.100 listan alkioiden läpikäynti
Tekijä: Oskari Heinonen
'''

def main():
    print('Give 5 numbers:')
    numbers = []
    for i in range(0,5):
        numbers.append(int(input('Next number: ')))
    print('The numbers you entered that were greater than zero were:')
    for i in numbers:
        if i > 0:
            print(i)

if __name__ == '__main__':
    main()