a = int(input("Skriv inn et tall: "))
b = int(input("Skriv inn et nytt tall: "))

ans1 = a*b
ans2 = a+b

if ans1 < ans2:
    print("I dette tilfellet gir multiplikasjon minst svar:", ans1)
elif ans1 == ans2:
    print("I dette tilfellet gir multiplikasjon og summering det samme svaret:", ans1)
else:
    print("I dette tilfellet gir summering minst svar:", ans2)


correctans = 3*4

ans = int(input("Hva er 3*4? "))

if ans == correctans:
    print("Det er korrekt!")
else:
    print("Det er feil")