def bsfirst(a,left,right,x) : 

    if  left <= right : 
        mid = (left + right)//2 

        if (mid == left or x > a[mid - 1]) and a[mid] == x  : 
            return mid 

        elif x > a[mid] : 
            return bsfirst(a,mid+1,right,x)
             

        else : 
            return bsfirst(a,left,mid -1 , x)  

    return -1 



if __name__ == '__main__' : 
    n,x = map(int,input().split()) 
    a = list(map(int,input().split())) 
    result = binary_search(a,0,n-1,x) 
    print(result) 
