def fastened_jasket() : 
    
    n = int(input())
    a = list(map(int,input().split()))


    
    # special case n = 1 

    if n == 1 : 
        if a[0] == 1 : 
            return 'YES'
        else : 
            return 'NO'
    
    if n > 1 :
        # if there are more than two number zeros  
        count = 0 

        for i in range(n) : 
            if a[i] == 0 : 
                count = count + 1 
        
        if count == 1 : 
            return 'YES'
        
        else : 
            return 'NO'
            
print(fastened_jasket())
