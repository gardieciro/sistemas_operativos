primos = [True] * 100
primos[0] = False
for i in range(1, 99): 
    if primos[i]: 
         for j in range(i+1, 100): 
            if (j+1) % (i+1) == 0: 
                primos[j] = False 
for i in range(100): 
    if primos[i]: print(i+1)