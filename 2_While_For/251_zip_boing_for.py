'''
COMP.CS.100 zip boing for
Tekijä: Oskari Heinonen
'''

def main():
    limit = int(input('How many numbers would you like to have? ')) + 1
    for i in range(1,limit):
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