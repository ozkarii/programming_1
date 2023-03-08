'''
COMP.CS.100 käännä nimet oikeinpäin 
Tekijä: Oskari Heinonen
'''


def reverse_name(name: str):
    '''
    Returns a comma separated name reversed.
    :param name: str, name to be separated
    '''
    name = name.split(',')
    name.reverse()
    i = 0
    while i < len(name):
        name[i] = name[i].strip()
        i += 1
    if len(name) < 2:
        return name[0]
    else:
        final =  ' '.join(name)
        while True:
            if final.startswith(' ') == True:
                final = final.replace(' ','')
            else:
                while True:
                    if final.endswith(' ') == True:
                        final = final.replace(' ','')
                    else:
                        return final

        


def main():
    print(reverse_name(" , Y "))

if __name__ == '__main__':
    main()