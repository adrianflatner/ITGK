poenggrenser = open('poenggrenser_2011.csv','r')

def alle(fil):
    poeng = open(fil, 'r')
    teller = 0
    for linje in poeng:
        if "Alle" in linje:
            teller += 1
    return teller


def gjennomsnitt(fil):
    poeng = open(fil,'r')
    teller = 0
    y = 0
    for linje in poeng:
        if "NTNU" in linje:
            if "Alle" not in linje:
                teller += 1
                x = float(linje.split(',')[1])
                y+=x

    gjsnitt = y/teller
    return round(gjsnitt,3)


def laveste_opptak_tall(fil):
    list = []
    poeng = open(fil,'r')
    for linje in poeng:
        if "Alle" not in linje:
            list.append(float(linje.split(',')[1]))
    return min(list)


def laveste_opptak(fil):
    poeng = open(fil, 'r')
    smallestInt = float('inf')
    for linje in poeng:
        if "Alle" not in linje:
            number = float(linje.split(',')[1])
            if smallestInt > number:
                smallestInt = float(linje.split(',')[1])
                ans = linje.split(',')[0]
    return ans


def main():

    print(alle('poenggrenser_2011.csv'))
    print(gjennomsnitt('poenggrenser_2011.csv'))
    print(laveste_opptak_tall('poenggrenser_2011.csv'))
    print(laveste_opptak('poenggrenser_2011.csv'))

main()