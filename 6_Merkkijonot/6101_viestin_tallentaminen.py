"""
COMP.CS.100 viestin tallentaminen
Tekijä: Oskari Heinonen
"""


def read_message() -> list:
    """
    Prompts user to input rows of text, returns a list of the inputted rows.
    No params
    :return: list, list of values inputted
    """
    msg_list = []
    while True:
        msg = input()
        if msg != '':
            msg_list.append(msg)
        else:
            return msg_list


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    msg_caps = []
    for i in msg:
        msg_caps.append(i.upper())
    print("The same, shouting:")
    for i in msg_caps:
        print(i)


if __name__ == "__main__":
    main()
