Normal_billet = 440
Minipris = 199

ans3 = ("ja" or "JA" or "Ja" or "jA")

dager = int(input("Hvor mange dager til du skal reise? "))

barn_u16 = Normal_billet/100*50
militærosv = Normal_billet/100*75
dobbel = Normal_billet/100*37.5
dobbel2 = Normal_billet/100*56.25
miniprisavslag = Minipris/100*90

if dager < 14:

    u_16 = input("Er du under 16 år? ")
    militær = input("Er du i militæret eller 60+? ")
    student = input("Er du student? ")

    if u_16 == ans3:

        if student == ans3:
            print ("Da får du 37,5% i rabatt: ", dobbel)
        else:
            print("Da får du 50% rabatt:", barn_u16)

    elif militær == ans3:
        if student == ans3:
            print("Da får du 56% i rabatt: ", dobbel2)
        else:
            print("Da får du 25% rabatt:", militærosv)

    elif student == ans3:
            print("Da får du 25% rabatt:", militærosv)

    else:
        print("Du må betale full pris:", Normal_billet)
else:

    student = input("Er du student? ")

    if student == ans3:
        print("Du får minipris og 10% avslag:", miniprisavslag )
    else:
        print("Du får minipris:", Minipris)

    onsk = (input("Denne kan ikke refunderes. Ønsker du heller full pris? "))
    if onsk == ans3:

        u_16 = input("Er du under 16 år? ")
        militær = input("Er du i militæret eller 60+? ")
        student = input("Er du student? ")

        if u_16 == ans3:

            if student == ans3:
                print("Da får du 37,5% i rabatt: ", dobbel)
            else:
                print("Da får du 50% rabatt:", barn_u16)

        elif militær == ans3:
            if student == ans3:
                print("Da får du 56% i rabatt: ", dobbel2)
            else:
                print("Da får du 25% rabatt:", militærosv)

        elif student == ans3:
            print("Da får du 25% rabatt:", militærosv)

        else:
            print("Du må betale full pris:", Normal_billet)
    else:
        print("Takk for pengene!")





