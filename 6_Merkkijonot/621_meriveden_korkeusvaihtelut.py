"""
COMP.CS.100 meriveden korkeusvaihtelut
Tekijä: Oskari Heinonen
Sähköposti: oskari.heinonen@tuni.fi
"""

from math import sqrt


def get_data() -> list:
    """
    Asks the user to input seawater levels until empty string is inputted.
    Returns data as a list. Prints only an error message
    if less than two inputs are given. No parameters.
    """
    print('Enter seawater levels in centimeters one per line.')
    print('End by entering an empty line.')
    data = []
    while True:
        i = input('')
        if i != '':
            data.append(float(i))
        elif len(data) < 2:
            print('Error: At least two measurements must be entered!')
            return
        else:
            return data


def median(data: list) -> float:
    '''
    Returns the median of the dataset.
    If list lenght is even, mean of the two middle numbers is returned.
    :param data: list, data list
    '''
    data.sort()
    if len(data) % 2 != 0:
        return data[int(len(data) / 2)]
    else:
        return (data[int(len(data) / 2 - 0.5)]
                + data[int(len(data) / 2 + 0.5)]) / 2


def mean(data: list) -> float:
    '''
    Returns the mean of the dataset.
    :param data: list, data list
    '''
    return sum(data) / len(data)


def variance(data: list) -> float:
    '''
    Returns the variance of the dataset.
    :param data: list, data list
    '''
    mean = sum(data) / len(data)
    # Calculating the sum term in the equation of variance
    var_sum = 0
    for i in data:
        var_sum += (i - mean) ** 2
    # Dividing the sum appropriately gives variance which is returned
    return var_sum / (len(data) - 1)


def std_dev(variance: float) -> float:
    '''
    Returns the standard deviation given the variance.
    :param variance: float, variance of the dataset
    '''
    return sqrt(variance)


def main():
    data = get_data()
    # If get_data() doesn't raise an error ie. returns a list, proceed
    if type(data) == list:
        print('Minimum:   ' + f"{min(data):.2f}" + ' cm')
        print('Maximum:   ' + f"{max(data):.2f}" + ' cm')
        print('Median:   ' + f"{median(data):.2f}" + ' cm')
        print('Mean:   ' + f"{mean(data):.2f}" + ' cm')
        print('Deviation:   ' + f"{std_dev(variance(data)):.2f}" + ' cm')
    else:
        return


if __name__ == '__main__':
    main()
