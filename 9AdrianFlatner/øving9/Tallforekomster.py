import pprint

def number_of_lines(filename):
    f = open(filename,'r')
    teller = 1
    linje = f.readline()
    while linje:
        linje = f.readline()
        teller += 1
    return teller



print(number_of_lines('numbers.txt'))

def number_frequency(filename):
    f = open(filename,'r')
    dic = {}

    for linje in f:
        linje = int(linje.rstrip("\n"))
        if linje not in dic.keys():
            dic[linje]=1
        else:
            count = dic[linje]
            dic[linje]=count+1
    return dic

d = (number_frequency('numbers.txt'))

pprint.pprint(d)
