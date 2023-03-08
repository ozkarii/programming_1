'''
COMP.CS.100 vuoden päivämäärät
Tekijä: Oskari Heinonen
'''

def main():
    month_data = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    month = 1
    while month <= 12:
        if month_data[month] == 31:
            for i in range(1,32):
                print(str(i) + '.' + str(month) + '.')
        elif month_data[month] == 30:
            for i in range(1,31):
                print(str(i) + '.' + str(month) + '.')
        else:
            for i in range(1,29):
                print(str(i) + '.' + str(month) + '.')
        month += 1
    

if __name__ == '__main__':
    main()