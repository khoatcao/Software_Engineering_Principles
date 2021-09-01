import random 
def array() : 

    a,b = list(map(int,input().split())) 
    
    k,m = list(map(int,input().split()))

    NA = list(map(int,input().split()))

    NB = list(map(int,input().split()))

    
            
    
    if NA[k-1] < NB[b- m] : 
        return 'YES'
    else : 
        return 'NO'  

    

print(array())