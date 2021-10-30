from queue import PriorityQueue 
MAX = 300000 + 5 
INF = 1e9 
class Node : 

    def __init__(self,_id,_dist) : 

        self.dist = _dist 

        self.id = _id 
    

    def __lt__(self,other) : 
        
        return self.dist <= other.dist

'''
def primmst() : 

    ans = 0 
    for i in range(n) : 

        if path[i] == -1 : 
            continue 

        ans += dist[i] 

    
    return ans 
'''


def prim(s) : 

    dist = [INF for _ in range(MAX)] 
    path = [-1 for _ in range(MAX)] 
    visited = [False for _ in range(MAX)] 

    pq = PriorityQueue() 

    pq.put(Node(0,s)) 

    dist[s] = 0 

    while pq.empty() == False : 

        u = pq.get().id 
        visited[u] = True 
        for neighbor in graph[u] :
            v  = neighbor.id 
            w = neighbor.dist 

            if visited[v] == False and w < dist[v] : 
                dist[v] = w 
                pq.put(Node(dist[v],v)) 

                path[v] = u  
    ans = 0 
    for i in range(n) : 

        if path[i] == -1  : 
            continue 

        ans += dist[i] 

    return ans 


if __name__ == '__main__' : 

    test = int(input()) 

    for _ in range(test) : 
   
        n = int(input()) 
        p = int(input()) 

        m = int(input()) 
        graph = [[] for _ in range(MAX)]
        for _ in range(m) : 
            u,v,w = map(int,input().split()) 

            u -=1 
            v -= 1 

            graph[u].append(Node(v,w)) 
            graph[v].append(Node(u,w))

   
        print(prim(0) * p )



