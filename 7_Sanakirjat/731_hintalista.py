"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Oskari Heinonen
Email: oskari.heinonen@tuni.fi

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        name = input("Enter product name: ").strip()
        if name in PRICES:
            print("The price of", name, "is", f"{PRICES[name]:.2f}", "e")
        elif name == "":
            print("Bye!")
            break
        else:
            print("Error:", name, "is unknown.")



if __name__ == "__main__":
    main()
