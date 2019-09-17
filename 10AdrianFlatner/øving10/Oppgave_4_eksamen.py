import random

def cold_days(templist):
    teller = 0
    for n in templist:
        if n < 0:
            teller += 1
    return teller

print('Antall dager under 0:',cold_days([1,-5,3,0,-6,-3,15,0]))

def cap_data(array,min_value,max_value):
    result = []
    for n in array:
        if n < min_value:
            result.append(min_value)
        elif n > max_value:
            result.append(max_value)
        else:
            result.append(n)
    return result

A = [-70,30,0,90,23,-12,95,12]
print('Result, cap data:',cap_data(A,-50,50))

def generate_testdata(N,min_value,max_value):
    #result = []
    #for n in range(N):
    #result.append(random.randint(min_value, max_value))
    result = (random.sample(range(min_value,max_value),N))
    return result

print('Generate testdata:',generate_testdata(10,-5,10))


temp = [1,5,3]
rain = [0,30,120]
humidity = [30,50,65]
wind = [3,5,7]

def create_db(temp,rain,humidity,wind):
    dic = {}
    for n in range(len(temp)):
        dic[n+1] = [temp[n], rain[n], humidity[n], wind[n]]
    return dic

print('Dictionary:',create_db(temp,rain,humidity,wind))

print('')


def print_db(weather):
    print("")
    print("DAY | temp | rain | humidity | wind ")
    print("====+======+======+==========+======")
    for day in weather:
        temp = weather[day][0]
        rain = weather[day][1]
        humidity = weather[day][2]
        wind = weather[day][3]

        print(format(day,'4d'),format(temp,'6d'),
        format(rain,'6d'),format(humidity,'10d'),
        format(wind,'6d'))

print_db(create_db(temp,rain,humidity,wind))




temp = [1,2,3,-5,-6,-7,-8,-9,3,0]
rain = [0,20,30,0,10,30,50,0,5,2]

print('')

def teller_synkende(list): #Teller dager under 0 samt synkende
    teller = 0
    for i in range(len(list)):
        if list[i]<0:
            if list[i] > list[i+1]:
                teller += 1
    return teller

def strange_weather(temp,rain):
    start = 0
    stop = 0
    for i in range(len(temp)):
        for a in range(len(rain)-1):
            if temp[i]<0:
                if temp[i] > temp[i+1] and rain[a] < rain[a+1]:
                    start = (i+1) - (teller_synkende(temp)-1)
                    stop = a
    return start,stop

a,b=strange_weather(temp,rain)
print('start:',a,'slutt:',b)


