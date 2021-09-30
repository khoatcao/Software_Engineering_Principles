def Chocolate_Consume() : 

    n = int(input())

    t = list(map(int,input().split()))

    i = 0 

    j = n - 1 
    alice_time = 0 
    bod_time = 0 
    a = []
    while i <= j : 

        if alice_time +  t[i]   <= bod_time +  t[j]  : 
            # update for alice 
            alice_time = alice_time + t[i] 
            i += 1  
        
        else : 
            bod_time = bod_time + t[j]
            j -= 1      
    a.append((i,n - i ))

    for name in a : 
        print(name[0],name[1])

    exit()

print(Chocolate_Consume())
        
    
    

