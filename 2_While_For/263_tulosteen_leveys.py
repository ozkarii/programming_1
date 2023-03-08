'''
COMP.CS.100 tulosteen leveys
Tekijä: Oskari Heinonen
'''

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:>3}", " ", end="")
        print()

if __name__ == "__main__":
    main()
