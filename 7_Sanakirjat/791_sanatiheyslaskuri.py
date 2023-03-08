"""
COMP.CS.100 Sanatiheyslaskuri
Tekijä: Oskari Heinonen
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    input_txt = input()
    txt_list = []
    while input_txt != "":
        words = input_txt.split()
        for word in words:
            txt_list.append(word.lower())
        input_txt = input()
    full_txt = sorted(txt_list)
    density_dict = {}
    for i in full_txt:
        density_dict[i] = str(full_txt.count(i)) + " times"
    for i in density_dict:
        print(i,":",density_dict[i])

if __name__ == '__main__':
    main()