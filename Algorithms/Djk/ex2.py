from queue import PriorityQueue 

MAX = 100 + 5 

INF = int(1e9)  + 7 

class Node : 

    def __init__(self,_id,_dist) : 

        self.id = _id 
        self.dist = _dist 

    def __lt__(self,other) : 

        return self.dist <= other.dist 



def ex3(s) : 

    pq = PriorityQueue()  
    pq.put(Node(s,0)) 
    dist[s] = 0 

    while not pq.empty() : 

        top = pq.get() 

        u = top.id 
        w = top.dist 

        for neighbor in graph[u] :

            if w + neighbor.dist <  dist[neighbor.id] : 
                dist[neighbor.id] = w + neighbor.dist 
                pq.put(Node(neighbor.id,dist[neighbor.id])) 
if __name__== '__main__' : 
    n=  int(input()) 
    e = int(input()) 
    t = int(input()) 
    m = int(input()) 
    graph = [[] for _ in range(MAX)]
    dist = [INF for _ in range(MAX)]
    for _ in range(m) : 
        a,b,w =  map(int,input().split()) 
        graph[b].append(Node(a,w)) 

    ex3(e)
    
    mouse = 0 
    for i in range(1,n+1) : 

        if dist[i] <= t : 
            mouse +=1 

    print(mouse) 

    



