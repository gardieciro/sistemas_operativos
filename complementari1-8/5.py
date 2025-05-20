print("ingrese la velocidad de ambos vehiculos")
v1=float(input("v1:"))
v2=float(input("v2:"))
print("ingrese la distancia que los separa")
d=float(input("distancia:"))

if v1>0 and v2>0:
    t=d/(v1+v2)
    print(t,"segundos")
else:
    print("error")