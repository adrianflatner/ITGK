def is_six_at_edge(x):

    if x[0] == 6 or x[len(x)-1] == 6:
        return True
    else:
        return False

my_list = [1,2,3,7,5]

print(is_six_at_edge(my_list))

def average(liste):
    return sum (liste)/len(liste)

gjennomsnitt = (average(my_list))
print(gjennomsnitt)

def median(x):
    x.sort()
    midten = int(len(x)/2)
    return x[midten]

medianen = median(my_list)
print(medianen)


