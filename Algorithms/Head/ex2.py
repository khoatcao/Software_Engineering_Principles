from queue import PriorityQueue 

def Qheap(n) :
    pq = PriorityQueue() 
    pq_remove = PriorityQueue()
    for _ in range(n) : 
        line = input() 
        if line[0] == '1' : 
           value = int(line.split()[1])
           pq.put(value)  
        elif  line[0] == '2' :
           value = int(line.split()[1]) 
           pq_remove.put(value) 

        else : 
            while not pq_remove.empty() and pq.queue[0] == pq_remove.queue[0] : 
               pq.get()
               pq_remove.get()
            
            print(pq.queue[0]) 

if __name__== '__main__' : 

    n = int(input()) 

    Qheap(n) 