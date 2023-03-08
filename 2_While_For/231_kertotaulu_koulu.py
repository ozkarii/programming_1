'''
COMP.CS.100 kertotaulu koulu
Tekijä: Oskari Heinonen
'''

def main():
    i = 1
    x = int(input('Choose a number: '))
    while i <= 10:
        print(str(i) + ' * ' + str(x) + ' = ' + str(i*x))
        i += 1

if __name__ == '__main__':
    main()