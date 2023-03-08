"""
COMP.CS.100 Tiedoston rivien numerointi
Tekijä: Oskari Heinonen
"""

def main():
    filename = str(input("Enter the name of the file: "))
    try:
        file = open(filename, "r")
    except OSError:
        print("There was an error in reading the file.")
        return
    i = 1
    for line in file:
        print(str(i), str(line).rstrip())
        i += 1
if __name__ == '__main__':
    main()