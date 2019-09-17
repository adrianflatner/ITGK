def seperate(numbers,threshold):
    a = []
    b = []
    for n in range(len(numbers)):
        if numbers[n] < threshold:
            a.append(numbers[n])
        else:
            b.append(numbers[n])

    return a,b

list1 = [1,2,3,4,5,6,7,8,9]
number = 4
a,b = seperate(list1,number)
print(a,b)


def multiplication_table(n):

    table = [[0 for col in range(n)]
             for row in range(n)]

    for y in range(n):
        for x in range(n):
            table[y][x] = ((x+1)*(y+1))
    return table

print(multiplication_table(4))

