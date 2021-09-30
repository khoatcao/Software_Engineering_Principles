from queue import PriorityQueue
pq_0 = PriorityQueue()
pq = PriorityQueue() 
h = [1,2,3,4,5]  
n = 5 
for i in range(n) : 
    pq_0.put(h[i])    
    pq.put(-h[i]) 
print(pq_0.queue)
print(pq.queue)
