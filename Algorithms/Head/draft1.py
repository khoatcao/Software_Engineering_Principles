from queue import PriorityQueue 
n = int(input())
a = list(map(int,input().split()))
pq = PriorityQueue()
for i in range(1,n+1) : 
    pq.put(i) 
print(pq.queue)
print(pq.get())