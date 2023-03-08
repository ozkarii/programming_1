'''
COMP.CS.100 inflaatiolaskin listoilla
Tekijä: Oskari Heinonen
'''

def main():
    # Luodaan lista, johon tallennetaan kuukausittainen inflaatioprosentti käyttäjön toimesta
    values = []
    i = 1
    while True:
        x = input('Enter inflation rate for month ' + str(i) + ': ')
        if x != '':
            values.append(float(x))
        else:
            break
        i += 1

    if len(values) == 0:
        print('Error: at least 2 monthly inflation rates must be entered.')
    elif len(values) == 1:
        print('Error: at least 2 monthly inflation rates must be entered.')
    # Luodaan lista changes, johon lisätään values-listan arvojen muutokset, jos values-listan pituus > 1
    else:
        changes = []
        i = 0
        while i <= len(values)-2:
            changes.append(values[i+1] - values[i])
            i += 1
        # Tulostetaan changes-listan suurin arvo
        print('Maximum inflation rate change was ' + str(max(changes)) + ' points.')

if __name__ == '__main__':
    main()