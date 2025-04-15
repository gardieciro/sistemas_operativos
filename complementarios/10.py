print("ingrese el valor de los puntos a(x1,x2,x3)")
x1=float(input("x1:"))
y1=float(input("x1:"))
z1=float(input("x1:"))

print("ingrese los valores del punto b(x2,y2,z2)")
x2=float(input("x2:"))
y2=float(input("y2:"))
z2=float(input("z2:"))

dis=((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5

print("la distancia es de:",dis) 