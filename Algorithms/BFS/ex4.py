from queue import Queue 

MAX = 100000 + 5 

visited = [False for _ in range(MAX)]

graph = [[] for _ in range(MAX)]

cat = [0 for i in range(MAX)]


def bfs(s,a,m) : 
    count = 0 
    q = Queue() 
    visited[s] = True 
    cat[s] = 0 

    q.put(s) 
    # xet dinh s co chua cat ko 
    cat[s] = (1 if a[s] == 1 else 0 )  
    # xet dinh ket u v     
    while not q.empty() : 

        u = q.get()

        for v in graph[u] : 
            if not visited[v] : 
                visited[v] = True 
                if a[v] == 1 : 
                   cat[v] = cat[u] + 1 

                if cat[v] <= m : 
                    if len(graph[v]) == 1 : 
                           count +=1 
                    else : 
                           q.put(v)

    return count  

n,m = map(int,input().split())

a = [None] + list(map(int,input().split()))

for _ in range(1,n) : 
    u,v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u) 


print(bfs(1,a,m))