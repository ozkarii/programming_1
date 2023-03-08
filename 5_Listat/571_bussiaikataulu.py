'''
COMP.CS.100 bussiaikataulu
Tekijä: Oskari Heinonen
'''

def next_bus(schedule: list,time: int):
    '''
    Returns a list of next three bus departure times with given schedule and current time.
    :param schedule: list, schedule of departure times as integers in a list
    :param time: int, current time as an integer
    '''
    next_times = []
    for i in schedule:
        if i >= time:
            next_times.append(i)
        else:
            pass    
    i = 0
    while len(next_times) < 3:
        next_times.append(schedule[i])
        i += 1
    return next_times

def main():
    schedule = [630,1015,1415,1620,1720,2000]
    time = int(input('Enter the time (as an integer): '))
    print('The next buses leave:')
    print(next_bus(schedule,time)[0])
    print(next_bus(schedule,time)[1])
    print(next_bus(schedule,time)[2])

if __name__ == '__main__':
    main()