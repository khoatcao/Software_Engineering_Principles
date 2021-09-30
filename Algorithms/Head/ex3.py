from queue import PriorityQueue 

def min_cost() : 
  pq = PriorityQueue() 
  while True :
    n = int(input()) 
    if n == 0 : 
      break  
      #a = list(map(int,input().split()))
    for i in input().split(): 
        pq.put(int(i)) 
        
    sum = 0 
    while pq.qsize() > 1 : 
          first = pq.get() 
          second = pq.get() 
          sum += first + second 
          pq.put(first + second)         
    print(sum)  
    pq.get()

if __name__ == '__main__' : 
  min_cost() 