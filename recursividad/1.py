c=-1
i=0
m=0
while c<0 or i<=0 or i>=100 or m<=0:
    c=int(input("Ingrese el Capital:"))
    i =int(input("Ingrse el interes:"))
    m=int(input("Ingrese el tiempo en años:"))
for i in range (m):
    c=c*(1+i/100)
print("tienes",c,"soles")