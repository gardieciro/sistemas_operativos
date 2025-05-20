print("ingrese el costo del articulo")
costo=float(input())

print("ingrese la marca")
m=input()

if costo>=2000 and m=="nosy":
    pa=costo*0.90
    pt=pa*0.95
elif costo>=200 and m!="nosy":
    pt=costo*0.90
elif costo<2000 and m=="nosy":
    pa=costo*0.95
    pt=pa+pa*0.20
elif costo<2000 and m!="nosy":
    pa=costo*1.20

print("usted pagara:",pt,"pesos")