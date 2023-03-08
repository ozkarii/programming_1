'''
COMP.CS.100 fibonacci
Tekijä: Oskari Heinonen
'''

def main():
    n1 = 1
    n2 = 1
    n = int(input('How many Fibonacci numbers do you want? '))
    i = 2
    print('1. ' + str(n1))
    print('2. ' + str(n2))

    while i < n:
        n3 = n1 + n2
        print(str(i + 1) + '. ' + str(n3))
        n1 = n2
        n2 = n3
        i += 1

if __name__ == '__main__':
    main()