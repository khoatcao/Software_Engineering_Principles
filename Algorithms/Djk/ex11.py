from queue import PriorityQueue
MAX = 100 
INF = int(1e9) 
class Node : 
    def __init__(self,id,dist) : 
        self.id = id 
        self.dist = dist 
    def __lt__(self,other) :
        return self.dist <= other.dist


def ex11(s) : 

    pq = PriorityQueue() 

    pq.put(Node(s,0)) 

    dist[s] = 0 

    while pq.empty() == False : 
        top = pq.get() 
        u = top.id 
        w = top.dist 

        for neighbor in graph[u] :

            if w + neighbor.dist < dist[neighbor.id] : 
                dist[neighbor.id] = w + neighbor.dist 
                pq.put(Node(neighbor.id,dist[neighbor.id])) 


if __name__ == '__main__' :  
    n = int(input())    
    graph = [[] for _ in range(n + 5)] 
    dist = [INF for _ in range(n+5)] 

    
    for _ in range(n) : 

        a,b,w = map(int,input().split()) 

        # create graph 

        graph[a].append(Node(b,w)) 
        graph[b].append(Node(a,w)) 


    
    s = int(input()) 

    ex11(s) 

    Q = int(input()) 

    for _ in range(Q) : 

        v = int(input()) 

        print(dist[v] if dist[v] != INF else 'NO PATH') 