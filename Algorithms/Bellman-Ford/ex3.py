INF = 10 ** 9
energy = [0] * 105 # weight array 
from queue import Queue 
class Edge : 
    def __init__(self,_source,_target) : 
        self.source = _source 
        self.target = _target 
# Bellman_Ford function 
def Bellman_Ford(s,f) : 
    dist = [-INF] * (n+1) 
    dist[1] = 100 
    for i in range(n-1) :
        for edge in graph :  
          u  = edge.source 
          v = edge.target 
        
          if dist[u] > 0  : 

            dist[v] = max(dist[u] + energy[v],dist[v]) 
    
    for edge in graph : # find positive cycle and has path from u ->  n 

         u  = edge.source 
         v  = edge.target 
        

         if (dist[u] > 0)    and (dist[u] + energy[v] > dist[v]) and bfs(u,n):   

            # update dist[v] 
            return True  

    return dist[f] > 0 
# function bfs to check whether has the path from the start to finish room 
def bfs(s,f) : 
    visited = [False] * (n+1) 
    q = Queue() 
    visited[s] = True 
    q.put(s) 

    while not q.empty() : 
        u = q.get() 
        for edge in graph :
            if edge.source  == u : 
                v = edge.target  
                if not visited[v] : 
                  visited[v] = True 
       
                if v == f : 

                   return True 
    
    return False  

if __name__ == '__main__' :    
    while True : 
        n = int(input()) 
        if n == -1 : 
            break 
        graph = [] 
        for u in range(1,n+1) : 

            line = list(map(int,input().split())) 
            energy[u] = line.pop(0) 
            
            if not line :
                line.extend(list(map(int,input().split()))) 

            m = line.pop(0) 

            while len(line) != m : 
                line.extend(list(map(int,input().split()))) 

            for v in line : 

                graph.append(Edge(u,v)) 


        print("winnable" if Bellman_Ford(1,n) else "hopeless")