'''
COMP.CS.100 zip boing while-loopilla
Tekijä: Oskari Heinonen
'''

def main():
    i = 1
    limit = int(input('How many numbers would you like to have? '))
    while i <= limit:
        if i % 3 == 0 and i % 7 == 0:
            print('zip boing')
        elif i % 3 == 0:
            print('zip')
        elif i % 7 == 0:
            print('boing')
        else:
            print(str(i))
        i += 1

if __name__ == '__main__':
    main()