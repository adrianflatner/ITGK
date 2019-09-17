def summerOlympics(firstYear,lastYear):

    OLar = list(range(1948,lastYear+1,4))
    inn = list(range(firstYear,lastYear+1))
    ut = []
    for a in inn:
            if a in OLar:
                ut.append(a)
    return ut

print(summerOlympics(1999,2012))

def findAge(bYear,bMonth,bDay):
    age = 0
    yyyy,mm,dd = current_date()
    if bMonth > mm:
        if bDay > dd:
            age = (yyyy-1)-bYear
    else:
        age = yyyy-bYear
    return age


def current_date():
    yyyy = 2017
    mm = 11
    dd = 13
    return yyyy,mm,dd

print(findAge(1996,12,15))


table = [['Adrian','Flatner',1996,15,1],
         ['George','Bush',1961,5,6],
         ['Justin','Bieber',1994,3,1]]


def printAgeDiff(table):
    for n in range(len(table)-1):
        age = findAge(table[n][2],table[n][3],table[n][4])
        age2 = findAge(table[n+1][2],table[n+1][3],table[n+1][4])
        if age==age2:
            print(table[n][1],table[n][2],'er like gammel som', table[n+1][1],table[n+1][2])
        elif age > age2:
            print(table[n][0],table[n][1],'er eldre enn', table[n+1][0],table[n+1][1])
        elif age < age2:
            print(table[n][0], table[n][1], 'er yngre enn', table[n + 1][0], table[n + 1][1])

printAgeDiff(table)

