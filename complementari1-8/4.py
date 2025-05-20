print("ingrese la fecha")
a=int(input("año:"))
m=int(input("mes:"))
d=int(input("dia:"))

if d>0 and d<30:
    print("mañana es:",d+1,m,a)
else:
    if m>0 and m<12:
        print("mañana es:",d,m+1,a)
    else:
        print("mañana es:",d,m,a+1)