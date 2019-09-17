def gcd(a,b):

    while b != 0:
        gammel_b = b
        b = a % b
        a = gammel_b
    return a


def reduce_fraction(a,b):

    x = a/gcd(a,b)
    y = b/gcd(a,b)
    return x, y

a,b = reduce_fraction(9,12)
print(format(a,'.0f'),"/",format(b,'.0f'),sep="")

