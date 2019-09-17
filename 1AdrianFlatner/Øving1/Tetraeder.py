import math

h = int(input("Velg høyde på tetraederet "))

a = (3/math.sqrt(6))*h
V = (math.sqrt(2)*a**3)/12
A = math.sqrt(3)*a**2

print("Et tetraeder med høyde ", h, " har overflatearealet ", format(A,".2f"), " og volumet ", format(V,".2f"),".", sep="")
