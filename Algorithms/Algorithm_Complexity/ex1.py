def find_maximum() : 
    n,t = list(map(int,input().split()))
    a = list(map(int,input().split())) 
    sum = 0 
    count = 0
    k = 0  
    for i in range(n) :
        sum += a[i] 
        if sum < t : 
            count += 1 
        else : 
            sum = sum - a[k] 
            k += 1 
    return count
print(find_maximum())
             
            

    