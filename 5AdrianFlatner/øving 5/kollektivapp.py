def sykkel_funksjon(a):
    if a == ("JA"):
        sykkelpris = 50
    else:
        sykkelpris = 0
    return sykkelpris

def billettpris():

    ans = str.upper("ja")
    while ans == str.upper("ja"):

        alder = int(input("Hva er din alder? "))
        sykkel = str.upper(input("Har du sykkel? "))

        svar = sykkel_funksjon(sykkel)


        if alder > 60:
            print("Honnør:", 0+svar, "kr")

        elif alder >= 26:
            print("Voksen", 80+svar, "kr")

        elif alder >= 21:
            print("Student", 50+svar,"kr")

        elif alder >= 5:
            print("Barn:", 20+svar, "kr")

        else:
            print("Småbarn", 0+svar, "kr")
        ans = str.upper(input("Vil du kjøpe flere billetter?"))

billettpris()

