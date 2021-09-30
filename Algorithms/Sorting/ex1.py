def Devu_Learning() : 


    n,x = list(map(int,input().split()))

    c = list(map(int,input().split()))

    c.sort()

    sum = 0 

    i = 0 

    t = 0 # save time point learning 

    

    for s in c : 
        t = s * x 
        sum +=  t 
        if x > 1 : 
            x -= 1 

    return sum  
print(Devu_Learning())

    