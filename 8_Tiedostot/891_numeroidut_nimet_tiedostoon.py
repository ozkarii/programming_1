"""
COMP.CS.100 
Tekijä: Oskari Heinonen
"""

def read_message() -> list:
    """
    Prompts user to input rows of text, returns a list of the inputted rows.
    No params
    :return: list, list of values inputted
    """
    msg_list = []
    print("Enter rows of text. Quit by entering an empty row.")
    while True:
        msg = input()
        if msg != '':
            msg_list.append(msg)
        else:
            return msg_list

def main():
    filename = input("Enter the name of the file: ")
    try:
        file = open(filename, "w")
    except FileNotFoundError:
        print("Writing the file", str(filename), "was not successful.")
        return
    data = read_message()
    count = 1 
    for i in data:
        print(str(count), str(i), file=file)
        count += 1
    print("File", str(filename), "has been written.")
if __name__ == '__main__':
    main()