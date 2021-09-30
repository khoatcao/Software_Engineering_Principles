from queue import Queue 

max = 1000 + 5 

graph = [[] for i in range(max)]
visited = [False for i in range(max)] 
dist = [0 for i in range(max)]

def bfs(s) : 
  
  q = Queue()
  visited[s] = True 
  q.put(s) 
  
  while not q.empty() : 
    u = q.get()
    for v in graph[u] : 
      if not visited[v] : 
        visited[v] = True 
        dist[v] = dist[u] + 6 
        q.put(v) 

Q = int(input())

for _ in range(Q) : 
  V,E = map(int,input().split())
  
  for i in range(max) : 
    graph[i].clear()
    visited[i] = False
    dist[i] = 0 
  
  for i in range(E) : 
    u,v = map(int,input().split())
    
    graph[u].append(v)
    graph[v].append(u)
    
  s = int(input())
  bfs(s)
  
  for i in range(1,V+1) : 
    if i == s : 
      continue
    print(  dist[i]  if visited[i] else -1, end = ' ') 
  print()
    
    
    
      
  
  