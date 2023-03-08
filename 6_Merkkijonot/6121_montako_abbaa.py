"""
COMP.CS.100 montako abbaa?
Tekijä: Oskari Heinonen
"""


def count_abbas(text: str) -> int:
    """
    Returns the number of times the substring "abba" appears in a string

    :param text: str, text to be searched
    :return: int
    """
    list_of_chars = []
    i = 0
    abba_counter = 0
    while True:
        if i == len(text):
            return abba_counter
        elif i <= 3:
            list_of_chars.append(text[i])
            i += 1
            if "".join(list_of_chars) == "abba":
                abba_counter += 1
            else:
                pass
        else:
            list_of_chars.append(text[i])
            list_of_chars.pop(0)
            i += 1
            if "".join(list_of_chars) == "abba":
                abba_counter += 1
            else:
                pass


def main():
    return None


if __name__ == '__main__':
    main()
