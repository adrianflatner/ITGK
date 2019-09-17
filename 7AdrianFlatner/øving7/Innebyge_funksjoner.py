import random

#my_randoms = random.sample(range(1,101),10)
#randoms = [random.randrange(1,101,1) for i in range(10)]

random_numbers = []

def random_numb(n):

    for i in range(n):
        random_numbers.append(random.randrange(1,101,1))
    return random_numbers

random_numbers = random_numb(10)
print(random_numbers)

telle = random_numbers.count(2)
print(telle)


#teller = 0
#for a in random_numbers:
#    if a == 2:
#        teller += 1
#print(teller)

sum = 0
for i in random_numbers:
    sum += i
print(sum)

print(sorted(random_numbers))

random_numbers.reverse()
print(random_numbers)