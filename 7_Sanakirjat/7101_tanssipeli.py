"""
COMP.CS.100  tanssipelien pisteet
Tekijä: Oskari Heinonen
"""

SONG_RESULT = {"Bubble dancer": 93.4, "The Game": 92.03, "Vertex": 75.3,
               "Lemmings on the Run": 86.2, "Da Roots": 96.02,
               "Charlene": 75.3, "Disconnected": 86.3, "Fly away": 87.32,
               "Hybrid": 63.9, "My favourite game": 89.45, "Oasis": 59.5,
               "Remember December": 96.3, "The beginning": 90.45,
               "Tribal Style": 87.45, "Why Me": 97.38, "Xuxa": 63.84,
               "Zodiac": 83.43, "Queen of Light": 75.12, "Mouth": 98.34,
               "Pandemonium": 79.31}

def calculate_average(scores: dict) -> float:
    """Calculates the average score of the given dictionary of scores
    :param scores: dict, dictionary of scores
    :return: float, average score
    """
    return sum(scores.values())/len(scores)

def main():
    print(calculate_average(SONG_RESULT))

if __name__ == '__main__':
    main()