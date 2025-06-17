v = [] 
n = int(input()) 
while True: 
    o = int(input()) 
    if o == 0: 
        break 
    if o == 1 and len(v) < n: 
        v.append(int(input())) 
    elif o == 2 and v: 
        x = int(input()) 
        if x in v: 
            v.remove(x) 
    elif o == 3: 
        print(v) 
    elif o == 4: 
        x = int(input()) 
        print(v.count(x)) 
    elif o == 5: 
        print("Media:", sum(v)/len(v), "Máximo:", max(v))