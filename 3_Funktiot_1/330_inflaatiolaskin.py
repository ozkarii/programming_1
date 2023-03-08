'''
COMP.CS.100 inflaatiolaskin
Tekijä: Oskari Heinonen
Sähköposti: oskari.heinonen@tuni.fi
'''

def main():
    # Määritellään tarvittavat muuttujat
    # value_1 on "edellinen" arvo (n) ja value_2 "seuraava" arvo (n + 1)
    # max_value -muuttujaan tallennetaan toistaiseksi suurin muutoksen arvo
    i = 1
    value_1 = None
    value_2 = None
    max_value = None
    while True:
        # Silmukan alussa tallennetaan aina edellisellä kierroksella
        # syötetty arvo (value_2) muuttujaan value_1, jonka jälkeen 
        # tallennetaan käyttäjän syöttämä arvo taas muuttujaan value_2.
        value_1 = value_2
        value_2 = input('Enter inflation rate for month ' + str(i) + ': ')
        if value_2 == '' and i == 1:
            print('Error: at least 2 monthly inflation rates must be entered.')
            break
        elif value_2 == '' and i == 2:
            print('Error: at least 2 monthly inflation rates must be entered.')
            break
        elif value_2 == '' and i > 2:
            print('Maximum inflation rate change was', f"{max_value:.1f}", 'points.')
            break
        elif i == 1:
            i += 1
        else:
            value_1 = float(value_1)
            value_2 = float(value_2)
            # Kun vasta 2 arvoa on syötetty, suurin muutos on aina
            # näiden kahden arvon erotus.
            # Jos tämänhetkisten arvojen erotus on suurempi, kuin tämänhetkinen
            # max_values, tallennetaan erotus max_values -muuttujaan.
            if i == 2:
                max_value = value_2 - value_1
                i += 1
            elif value_2 - value_1 > max_value:
                max_value = value_2 - value_1
                i += 1
            else:
                i += 1

if __name__ == '__main__':
    main()