n = int(input()) 
v = [input() for _ in range(n)] 
for i in range(n // 2): 
    v[i], v[n - 1 - i] = v[n - 1 - i], v[i] 
print(v)