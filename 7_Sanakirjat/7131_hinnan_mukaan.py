"""
COMP.CS.100 lajittelu hinnan mukaan
Tekijä: Oskari Heinonen
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def payload(key):
    """Returns payload of the key
    :param key: Any, key of the dict
    :return: Any, payload
    """
    return PRICES[key]

def main():
    for product in sorted(PRICES,key=payload):
        print(product, f"{float(PRICES[product]):.2f}")

if __name__ == "__main__":
    main()
