"""
COMP.CS.100 Pisteiden lasketaa
Tekijä: Oskari Heinonen
"""

def main():
    filename = input("Enter the name of the score file: ")
    try:
        file = open(filename, "r")
    except (OSError, FileNotFoundError) :
        print("There was an error in reading the file.")
        return
    data = {}
    for line in file:
        line_list = str(line).split()
        try:
            key, payload = str(line_list[0]), int(line_list[1])
        except IndexError:
            print("There was an erroneous line in the file:")
            print(str(line))
            return
        except ValueError:
            print("There was an erroneous score in the file:")
            print(str(line_list[1]))
            return
        if key in data:
            data[key.strip()] = data[key.strip()] + int(str(payload).strip())
        else:
            data[key.strip()] = int(str(payload).strip())
    data_sorted = sorted(data)
    print("Contestant score:")
    for key in data_sorted:
        print(key, str(data[key]))

if __name__ == '__main__':
    main()