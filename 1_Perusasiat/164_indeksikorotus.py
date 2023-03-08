"""
COMP.CS.100 indeksikorotus
Tekijä: Oskari Heinonen
Opiskelijanumero: 151242115
"""

current_benefits = float(input('Enter the amount of the study benefits: '))
index_raise = 0.0117
after_raise_1 = current_benefits + current_benefits*index_raise
after_raise_2 = after_raise_1 + after_raise_1*index_raise

print('If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be ' + str(after_raise_1) + ' euros' + 
'\nand if there was another index raise, the study\nbenefits would be as much as ' + str(after_raise_2) + ' euros')

