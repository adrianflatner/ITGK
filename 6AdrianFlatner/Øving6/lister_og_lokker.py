number_list=[]
sum = 0

for i in range(100):
    number_list.extend([i])

for n in range(len(number_list)):
    if number_list[n]%3 == 0 or number_list[n]%10 == 0:
        sum += number_list[n]

print(number_list)
print(sum)

number_list2 = []+number_list

for a in number_list:

    if number_list[a] % 2 == 0:
        number_list[a] = number_list2[a+1]
    else:
        number_list[a] = number_list2[a-1]
print(number_list)

reversed_list = [] + number_list

for b in number_list and number_list2:
    number_list[b] -= 99
    number_list[b] *= (-1)
print(number_list)



