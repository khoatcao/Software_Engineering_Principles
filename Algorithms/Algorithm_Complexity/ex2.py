def George_and_Round() : 
    n,m = list(map(int,input().split()))

    a = list(map(int,input().split()))

    b = list(map(int,input().split()))
    
    count = i = 0 

    for j in range(m) : 
        if i >= n : 
            break 
        if b[j] >= a[i] : 
            count += 1 
            i += 1 
    return n - count 
print(George_and_Round())