"""
COMP.CS.100 kokonaisen viestin ROT13 -salaus
Tekijä: Oskari Heinonen
"""


def read_message() -> list:
    """
    Promts user to input rows of text, returns a list of the inputted rows.
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


def encrypt(text: str):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]
    if text in regular_chars:
        return encrypted_chars[regular_chars.index(text)]
    else:
        text = text.lower()
        if text in regular_chars:
            return encrypted_chars[regular_chars.index(text)].upper()
        else:
            return text


def row_encryption(text: str):
    """
    Encrypts a string by applying the encrypt() function to
    every character of the string.

    :param text: str, string to be encrypted
    :return: str, encrypted <text>
    """
    char_list = []
    for char in text:
        char_list.append(char)
    for index, item in enumerate(char_list):
        char_list[index] = encrypt(item)
    text = ''.join(char_list)
    return text


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    encrypted_msg = []
    for i in msg:
        encrypted_msg.append(row_encryption(i))
    print("ROT13:")
    for i in encrypted_msg:
        print(i)


if __name__ == '__main__':
    main()
