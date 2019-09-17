from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
opp_eller_ned = input("Ønsker du trekanten opp eller ned (O / N?) ")

pensize(7)
#pencolor("pink")
bgcolor("#00509e")


penn = input("Velg farge på pennen: NTNU-lilla eller NTNU-gul (L / G)? ")

if penn == ("L"):
    pencolor("#559288")
elif penn == ("G"):
    pencolor("#d5d10e")
else:
    print("Det kan du ikke velge mellom.")

fill = input("Hvilken farge vil du ha på fyllet i trekanten? NTNU-grå(GR), NTNU-gull(GU), eller NTNU-brun(B)? ")

if fill == ("GR"):
    fillcolor("#dfd8c5")
elif fill == ("GU"):
    fillcolor("#ccbd8f")
elif fill == ("B"):
    fillcolor("#90492d")
else:
    print("Dette kan du ikke velge mellom.")

if opp_eller_ned == ("O"):
    begin_fill()
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)
    end_fill()
elif opp_eller_ned == ("N"):
    begin_fill()
    forward(200)
    left(-120)
    forward(200)
    left(-120)
    forward(200)
    end_fill()
else:
    print("Det var et tullesvar")