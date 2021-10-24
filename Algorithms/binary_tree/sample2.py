# using de quy 

def binary_search(a,left,right,x) : 

    if left <= right : 

        mid = (left + right )//2

        if a[mid] == x : 
            return mid 
        
        if a[mid] > x : 
            return  binary_search(a,left,mid-1,x)

        
        return binary_search(a,mid+1,right,x) 

    return -1 


if __name__ == '__main__' : 

    n,x = map(int,input().split()) 
    a = list(map(int,input().split())) 

    result = binary_search(a,0,n-1,x)  

    print(result) 