'''
COMP.CS.100 TGIF
Tekijä: Oskari Heinonen
'''

def main():
    month_data = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    first_fridays = [0,3,7,7,4,2,6,4,1,5,3,7,5]
    month = 1
    while month <= 12:
        if month_data[month] == 31:
            c = first_fridays[month] - 5
            for i in range(1,32):
                if c % 7 == 0:
                    print(str(i) + '.' + str(month) + '.')
                    c += 1
                else:
                    c += 1
        elif month_data[month] == 30:
            for i in range(1,31):
                print(str(i) + '.' + str(month) + '.')
        else:
            for i in range(1,29):
                print(str(i) + '.' + str(month) + '.')
        month += 1

if __name__ == '__main__':
    main()