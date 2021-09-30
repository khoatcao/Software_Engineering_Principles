from queue import Queue 


MAX = 100000 + 5 
Mod = 100000 
dist = [-1 for i in range(MAX)]
def bfs(s,l) : 

    q = Queue() 
    q.put(s) 
    dist[s] = 0
    while not q.empty() : 
        u = q.get() 

        for x in a : 
            v = (x * u) % Mod 
            
            if dist[v] == -1 : 
                dist[v] = dist[u] + 1 
                q.put(v) 

                if v == l : 
                    return dist[v] 

    return -1 
s,l = map(int,input().split())

n = int(input())

a = list(map(int,input().split())) 

print(bfs(s,l))