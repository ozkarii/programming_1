'''
COMP.CS.100 vaihtorahat 
Tekijä: Oskari Heinonen
Opiskelijanumero: 151242115
'''

def main():
    purchase_price = int(input('Purchase price: '))
    paid_money = int(input('Paid amount of money: '))

    change = paid_money - purchase_price
    
    if change <= 0:
        print('No change')
    else:
        print('Offer change:')
        
        amount_10 = change // 10
        if amount_10 != 0:
            print(str(amount_10) + ' ten-euro notes')

        amount_5 = (change - amount_10*10) // 5
        if amount_5 != 0:
            print(str(amount_5) + ' five-euro notes')

        amount_2 = (change - (amount_10*10 + amount_5*5)) // 2
        if amount_2 != 0:
            print(str(amount_2) + ' two-euro coins')

        amount_1 = (change - (amount_10*10 + amount_5*5 + amount_2*2)) // 1
        if amount_1 != 0:
            print(str(amount_1) + ' one-euro coins')
    
if __name__ == '__main__':
    main()