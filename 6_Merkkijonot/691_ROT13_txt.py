"""
COMP.CS.100 ROT13
Tekijä: Oskari Heinonen
"""


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
