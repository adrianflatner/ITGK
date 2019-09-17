

antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0

kjonn = 0
alder = 0
fag = 0
variabelmedlem_ITGK = 0
timer_lekser = 0

def sjekk_svar(spm, a):

    if spm == "m":
        a += 1
        return a
    else:
        a += 0
        return a

def sjekk2_svar(spm, a):

    if spm == "f":
        a += 1
        return a
    else:
        a += 0
        return a

def les_ja_nei(spm,a):

    if spm == str.upper("ja"):
        a += 1
        return a

def les_tall(spm,a):
    a += spm
    return a

def skriv_statistikk():
    print("")
    print("Antall menn:", antall_menn)
    print("Antall kvinner:", antall_kvinner)
    print("Antall som tar fag:", antall_fag)
    print("Antall som tar ITGK:", antall_ITGK)
    print("Totalt antall timer lekser:", antall_timer_lekser)
    print("Gjennomsnitt lekser: ", antall_timer_lekser/(antall_kvinner+antall_menn))

x=0
def hade(spm):
    if spm == ("hade"):
        x = 1
    else:
        x = 0
    return x

while str.upper(input("Press enter for å starte, eller skriv 'hade' for å avslutte: ")) != str.upper("hade"):

    kjonn = input("Kjønn(m/f):")
    #x = hade(kjonn)
    alder = int(input("Alder: "))

    if 16 <= alder <=25:
        fag = str.upper(input("Tar du et fag? "))

        while fag != str.upper("ja"):
            fag = str.upper(input("Tar du et fag? "))

        if fag == str.upper("ja"):
            if alder < 22:
                variabelmedlem_ITGK = str.upper(input("Tar du ITGK? "))
            else:
                variabelmedlem_ITGK = str.upper(input("Tar virkelig du ITGK? "))
            timer_lekser = int(input("Hvor mange timer bruker du i snitt daglig på lekser? "))

    else:
        print("Du kan ikke ta undersøkelsen")



    antall_fag = les_ja_nei(fag, antall_fag)
    antall_ITGK = les_ja_nei(variabelmedlem_ITGK, antall_ITGK)
    antall_menn = sjekk_svar(kjonn, antall_menn)
    antall_kvinner = sjekk2_svar(kjonn, antall_kvinner)
    antall_timer_lekser = les_tall(timer_lekser, antall_timer_lekser)




skriv_statistikk()


