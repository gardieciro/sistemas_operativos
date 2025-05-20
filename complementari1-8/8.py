pi=3.1416

print("ingrese valores del menu:")
print("1:area del triangulo:")
print("2:area del circulo")
opc=int(input("opc:"))

if opc==1:
    print("area del triangulo")
    print("ingrese el lado del triangulo")
    l=float(input("l:"))
    a=((3**0.5)/4) *l**2
    print("el area del triangulo es:",a)

elif opc==2:
    print("area del circulo:")
    print("ingrese el radio del circulo")
    r=float(input("r:"))
    c=pi*r**2
    print("el area del circulo es:",c)

else:
    print("error")