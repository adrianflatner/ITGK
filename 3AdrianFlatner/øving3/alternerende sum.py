n = int(input("Skriv inn et heltall: "))
k = int(input("Velg et tall som max: "))

i = 1
sum = 0

while i <= n:

    if sum < k:
        if i%2:
            sum += i**2 #oddetall
        else:
            sum -= i**2
    else:
        break
    i += 1

print(sum)
