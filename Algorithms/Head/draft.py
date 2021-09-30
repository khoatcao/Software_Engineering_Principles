from queue import PriorityQueue 

def min_cost(n): 
  pq = PriorityQueue() 
  pq_sum = PriorityQueue()
  while True : 
    if n == 0 : 
      break 
    sum = 0 
    for i in range(1,n+1) :

      pq.put(a[i]) 
    
    print(pq.queue)
      
      #first = pq.get() 
      #second = pq.get() 
      
      #sum = first + second 
      #pq_sum.put(sum) 

      #cost = pq.get() + pq_sum().get() 

      
  

  
if __name__ == '__main__' : 
  n = int(input())
  a = list(map(int,input().split()))
  min_cost(n) 