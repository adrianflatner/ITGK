resultat = 0
Interasjoner = int(input("Velg interasjoner: "))


for gange in range(1,Interasjoner+1):
    print(gange,"-gangen:", sep="")

    for n in range(1,Interasjoner+1):
        resultat = gange*n
        print(resultat)
    print("")

