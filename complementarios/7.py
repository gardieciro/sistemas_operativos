import os, math
os.system ("cls")
pi=3.1416

b=float(input("ingrese el primer lado:"))
c=float(input("ingrese el segundo lado:"))
alfa=float(input("ingrese el angulo en grados sexagesimales:"))

a=(b**2+c**2-2*b*c math.cos(alfa*pi/180))**0.50
print("el lado a es de:",a)