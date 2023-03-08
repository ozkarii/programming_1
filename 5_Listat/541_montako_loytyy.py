'''
COMP.CS.100 montako löytyy
Tekijä: Oskari Heinonen
'''

def input_to_list(n: int):
    '''
    Prompts the user to input numbers n times determined by the parameter.
    Returns a list of inputted numbers
    :param n: int, how many numbers should be inputted
    '''
    numbers = []
    for i in range(0,n):
        number = int(input())
        numbers.append(number)
    return numbers
        



def main():
    n = int(input("How many numbers do you want to process: "))
    print('Enter',str(n),'numbers:')
    numbers = input_to_list(n)
    x = int(input('Enter the number to be searched: '))
    x_count = numbers.count(x)
    if x_count > 0:
        print(str(x),'shows up',str(x_count),'times among the numbers you have entered.')
    else:
        print(str(x),'is not among the numbers you have entered.')

if __name__ == '__main__':
    main()