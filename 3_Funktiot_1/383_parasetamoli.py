'''
COMP.CS.100 parasetamolin annostelu
Tekijä: Oskari Heinonen
'''

def calculate_dose(weight: int, time: int, total: int) -> int:
    '''
    Calculates the recommended dosage of parasetamol.
    :param weight: int, patient's weight
    :param time: int, time passed from previous dose
    :param total: int, total dose of last 24h
    '''
    if time < 6:
        return 0
    else:
        amount = 15 * weight 
        if amount + total > 4000:
            return 4000 - total
        else:
            return amount


def main():
    weight = input("Patient's weight (kg): ")
    time = input("How much time has passed from the previous dose (full hours): ")
    total = input("The total dose for the last 24 hours (mg): ")
    print("The amount of Parasetamol to give to the patient:", calculate_dose(int(weight),int(time),int(total)))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)



if __name__ == "__main__":
  main()
