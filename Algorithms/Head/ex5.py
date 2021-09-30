import heapq 


def ex5(n) : 
    
    maxHeap = [] 
    minHeap = [] 
    index = 0 
    total_price  = 0 
    taken = [False] * 10000 

    for _ in range(n) : 
        a = list(map(int,input().split())) 

        for x in a[1:] : 

            index += 1 

            heapq.heappush(maxHeap,(-x,index)) 

            heapq.heappush(minHeap,(x,index)) 


        while(taken[maxHeap[0][1]]) : 
            heapq.heappop(maxHeap) 

        
        while(taken[minHeap[0][1]]) : 
            heapq.heappop(minHeap) 

        
        taken[maxHeap[0][1]] = taken[minHeap[0][1]] = True 

        total_price += -heapq.heappop(maxHeap)[0] - heapq.heappop(minHeap)[0] 

    print(total_price) 
if __name__ == '__main__' : 
    n = int(input()) 

    ex5(n) 