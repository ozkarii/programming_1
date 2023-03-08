'''
COMP.CS.100 vokaalit ja konsonantit
Tekijä: Oskari Heinonen
'''

def main():
    vowels = "AaEeIiOoUuYy"
    word = input("Enter a word: ")
    vowel_count = 0
    consonant_count = 0
    for i in word:
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    print('The word "' + word + '" contains' , str(vowel_count) , "vowels" , "and" , str(consonant_count) , "consonants.")

if __name__ == '__main__':
    main()