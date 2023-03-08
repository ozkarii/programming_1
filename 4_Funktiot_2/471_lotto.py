'''
COMP.CS.100 lottopelejä
Tekijä: Oskari Heinonen
'''

def factorial(x: int) -> int:
    '''
    Returns the factorial of given integer.
    :param x: int
    '''
    n = 1
    for i in range(1,x + 1):
        n = i * n
    return n

def lotto_probability(n: int,p: int) -> str:
    '''
    Returns the probability to hit the jackpot in a lottery.
    :param n: int, the total number of balls in the lottery
    :param p: int, the number of balls drawn in the lottery 
    '''
    prob = round(factorial(n)/(factorial(n-p)*factorial(p)))
    prob = '1/' + str(prob)
    return prob


def main():
    n = int(input('Enter the total number of lottery balls: '))
    p = int(input('Enter the number of the drawn balls: '))
    if n < 0 or p < 0:
        print('The number of balls must be a positive number.')
    elif n < p:
        print('At most the total number of balls can be drawn.')
    else:
        print('The probability of guessing all',str(p),'balls correctly is',lotto_probability(n,p))

if __name__ == '__main__':
    main()