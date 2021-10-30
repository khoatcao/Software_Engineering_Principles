def isgood(a,x) : 
    sum = 0 
    for item in a : 
        sum += max(0,item - x )
    return sum 

def binary_search(a,left,right,k) : 

    while left <= right : 

        mid = (left + right)//2
        
                
        if isgood(a,mid) >= k  :  
            ans  = mid 
            left = mid - 1 
        else : 
            right = mid + 1 

    
    return ans  


if __name__ == '__main__' : 

    n,m = map(int,input().split()) 

    a = list(map(int,input().split()))

    left = 1 
    right = max(a) 
    print(binary_search(a,left,right,m)) 



