import random
n = int(input("Velg øvre grense: "))
random_number = random.randint(1,n)


gjett = int(input("Gjett hvilket tall jeg tenker på: "))

while random_number != gjett:
    if gjett < random_number:
        print("Det er for lavt")
    else:
        print("Det er for høyt")

    gjett = int(input("Gjett igjen: "))

print("Det stemmer!")