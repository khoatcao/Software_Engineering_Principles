from queue import PriorityQueue


MAX = 105 

INF = int(1e9) 

class Node : 

    def __init__(self,_id,_dist) : 
         self.id = _id 
         self.dist = _dist 

    def __lt__(self,other) : 

        return self.dist <= other.dist 

def Dijkstra(start) : 

    pq = PriorityQueue() 
    pq.put(Node(start,0)) 
    dist[s] = 0 
    dist[d] = 0 

    while not pq.empty() : 

        disttoU, u = pq.get() 

        if (disttoU != dist[u]) : 
            continue 
        
        for v in graph[u] : 

            if (dist[v] > dist[u] + 1) : 
                dist[v] = dist[u] + 1 
                pq.put(Node(v,dist[v])) 
        
            
if __name__== '__main__' : 
        t = int(input())

        for _ in range(1,t+1) : 

           n = int(input()) 

           graph = [[] for _ in range(MAX)] 

           dist = [INF for _ in range(MAX)]

           r = int(input()) 

           for _ in range(r) : 
            u,v = map(int,input().split()) 
            graph[u].append(Node(v))
            graph[v].append(Node(u))  
                
        
        s,d = map(int,input().split())

        distfroms = Dijkstra(s) 
        distfromd = Dijkstra(d) 


        ans = 0 

        for i in range(n) : 

            if ans < distfroms + distfromd : 
                ans = distfroms + distfromd 
        

        print("Case {}: {}".format(case,ans)) 

                


        
        
