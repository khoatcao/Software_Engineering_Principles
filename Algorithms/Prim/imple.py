from queue import PriorityQueue 

INF = 1e9 
MAX = 10000 + 5 
class Node : 
  
  def __init__(self,_id,_dist) : 
    self.dist = _dist 
    self.id = _id 
    
  def __lt__(self,other) : 
    
    return self.dist <= other.dist 

  
# print minimum spanning tree 

def printmst() : 
  ans = 0 
  for i in range(n) : 
    if path[i] == -1 : 
      continue 
      
    ans += dist[i] 
    print("{0} - {1}: {2} ".format(path[i],i,dist[i])) 
  print("Weight of mst: {0}".format(ans)) 
  
def prims(src) : 
  
  pq = PriorityQueue() 
  pq.put(Node(src,0)) 
  dist[src] = 0 
  while pq.empty() == False : 
    top = pq.get() 
    u = top.id 
    visited[u] = True 
    
    for neighbor in graph[u] : 
      v = neighbor.id 
      w = neighbor.dist 
      
      if visited[v] == False and w < dist[v] : 
        
        dist[v] = w 
        pq.put(Node(v,w)) 
        
        path[v] = u 
if __name__ == "__main__" : 
  
  n,m = map(int,input().split())
  graph  = [[] for i in range(n)] 
  dist = [INF for _ in range(n)] 
  
  path = [-1 for _ in range(n)]
  
  visited = [False for _ in range(n)] 
  
  for i in range(m) : 
    u,v,w = map(int,input().split()) 
    
    graph[u].append(Node(v,w)) 
    graph[v].append(Node(u,w)) 
  prims(1)  
  printmst()
  