import random

numbers = []
lotto_result = []
lotto_result2 = []


###############Funksjoner:

def lotto():
    print("\nAntall riktige tall:", antall_like, "\nAntall riktige tilleggstall:", antall_like2)

    print("")
    if antall_like == 7:
        print("Du har vunnet 2 749 455 kroner!")
    elif antall_like == 6 and antall_like2 >= 1:
        print("Du har vunnet 102 110 kroner!")
    elif antall_like == 6:
        print("Du har vunnet 3 385 kroner!")
    elif antall_like == 5:
        print("Du har vunnet 95 kroner!")
    elif antall_like == 4 and antall_like2 >= 1:
        print("Du har vunnet 45 kroner!")
    else:
        print("Du vant dessverre ingenting denne gangen.")

    print("")
    print("Din rekke:", myGuess, "+", myGuess2)
    print("Vinnertall:", lotto_result, "+", lotto_result2)
    print("")


def trekk(til, fra, n):
    for a in range(n):
        til.append(fra.pop(random.randint(0, len(fra) - 1)))


def complist(a, b):
    like_tall = 0

    for element in a:
        if element in b:
            like_tall += 1
    return like_tall


################


while input("Hei og velkommen til Lotto! Press enter for å begynne!\n (eller 'q' for å avslutte)") != ("q"):

    for i in range(1, 35):
        numbers.extend([i])

    myGuess = [int(input("Tippetall: ")), int(input("Tippetall: ")), int(input("Tippetall: ")),
               int(input("Tippetall: ")), int(input("Tippetall: ")), int(input("Tippetall: ")),
               int(input("Tippetall: "))]
    myGuess2 = [int(input("Tilleggstall: ")), int(input("Tilleggstall: ")), int(input("Tilleggstall: "))]

    trekk(lotto_result, numbers, 7)
    trekk(lotto_result2, numbers, 3)

    compare = set(myGuess).intersection(lotto_result)
    # print(compare)

    antall_like = complist(myGuess, lotto_result)
    antall_like2 = complist(myGuess2, lotto_result2)

    lotto()

