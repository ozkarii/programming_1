'''
COMP.CS.100 kertotaulu sataan
Tekijä: Oskari Heinonen
'''

def main():
    i = 1
    x = int(input('Choose a number: '))
    p = 0
    while p <= 100:
        p = i*x
        print(str(i) + ' * ' + str(x) + ' = ' + str(p))
        i += 1

if __name__ == '__main__':
    main()