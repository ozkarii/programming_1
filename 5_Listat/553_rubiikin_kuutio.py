'''
COMP.CS.100 rubiikin kuutio -kilpailut
Tekijä: Oskari Heinonen
'''

def result_input():
    '''
    Asks the user to input the 5 results and returns them as a list.
    '''
    results = []
    for i in range(0,5):
        results.append(float(input("Enter the time for performance " + str(i + 1) + ": ")))
    return results


def result_handler(results: list):
    '''
    Gets rid of the list's highest and lowest values and returns the mean of remaining values.
    :param results: list, list of the results to be handled
    '''
    results.remove((min(results)))
    results.remove((max(results)))
    return sum(results)/len(results)


def main():
    print("The official competition score is", f"{result_handler(result_input()):.2f}","seconds.")
    
if __name__ == '__main__':
    main()