'''
COMP.CS.100 listan indeksien läpikäyminen
Tekijä: Oskari Heinonen
'''

def main():
    print('Give 5 numbers:')
    numbers = []
    for i in range(0,5):
        numbers.append(int(input('Next number: ')))
    print('The numbers you entered, in reverse order:')
    for i in range(1,6):
        print(numbers[-i])
    

if __name__ == '__main__':
    main()