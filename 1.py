v1 = [int(input()) for _ in range(3)] 
v2 = [int(input()) for _ in range(3)] 
escalar = sum(v1[i]*v2[i] for i in range(3)) 
print("Producto escalar:", escalar) 
x = v1[1]*v2[2] - v1[2]*v2[1] 
y = -(v1[0]*v2[2] - v1[2]*v2[0]) 
z = v1[0]*v2[1] - v1[1]*v2[0] 
print("Producto vectorial:", x, "i", y, "j", z, "k")