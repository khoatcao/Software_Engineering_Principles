from queue import PriorityQueue 

def find_product(n,a) : 
     
    pq = PriorityQueue()  # default min heap 

    for i in range(n) : 
        pq.put(-a[i]) # max heap  
        
        if i < 2 : 
            print(-1) 
        
        else :
            # thao tac nhu cay max heap
            # lay top 3 gia tri lon nhat tu cay max heap  
            first = -pq.get()
            second = -pq.get() 
            third = -pq.get() 

            product = first*second*third 
            print(product) 
            # them phan tu moi vao mang 
            # complexity : O(nlog(n))
            #  
            pq.put(-first) 
            pq.put(-second) 
            pq.put(-third) 

    
if __name__ == '__main__' : 

    n = int(input()) 
    a = list(map(int,input().split()))
    find_product(n,a)  
    