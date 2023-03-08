"""
COMP.CS.100 turistisanakirja matkailijalle
Tekijä: Oskari Heinonen
"""


def main():
    english_spanish = {"hey": "hola", "home": "casa", "thanks": "gracias"}
    print("Dictionary contents:")
    eng_spa_content = []
    for i in sorted(english_spanish):
        eng_spa_content.append(i)
    print(", ".join(eng_spa_content))
    
    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")
        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish.get(word))
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng_add = input("Give the word to be added in English: ")
            spa_add = input("Give the word to be added in Spanish: ")
            english_spanish[eng_add] = spa_add
            print("Dictionary contents:")
            eng_spa_content = []
            for i in sorted(english_spanish):
                eng_spa_content.append(i)
            print(", ".join(eng_spa_content))
        elif command == "R":
            word_remove = input("Give the word to be removed: ")
            if word_remove in english_spanish:
                del english_spanish[word_remove]
            else:
                print("The word", word_remove, "could not be found from the dictionary.")

        elif command == "Q":
            print("Adios!")
            return

        elif command == "P":
            english_spanish_sorted = sorted(english_spanish)
            spanish_english = {v: k for k, v in english_spanish.items()}
            spanish_english_sorted = sorted(spanish_english)
            print()
            print("English-Spanish")
            for item in english_spanish_sorted:
                print(item,english_spanish[item])
            print()
            print("Spanish-English")
            for item in spanish_english_sorted:
                print(item,spanish_english[item])
            print()

        elif command == "T":
            words = input("Enter the text to be translated into Spanish: ").split()
            final_list = []
            for i in words:
                if i in english_spanish:
                    final_list.append(english_spanish.get(i))
                else:
                    final_list.append(i)
            print("The text, translated by the dictionary:")
            print(' '.join(final_list))

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
