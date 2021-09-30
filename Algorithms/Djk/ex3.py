from heapq import heappush, heappop 


def Dijkstra(s,f) : 

    dist = [10 ** 9 ] * (n+1)

    pq = [(0,s)] 

    dist[s] = 0 

    while pq : 

        w,u = heappop(pq)
        if u == f : 
            break 

        for v,weight in graph[u] :

            if w + weight < dist[v] : 

                dist[v] = w + weight 

                heappush(pq,(dist[v],v)) 
    
    return dist[f] 
if __name__ == '__main__' :

    T = int(input()) 
    for t in range(T) : 
        n = int(input())
        graph = [[] for _ in range(n+1)]
        cities = [] 

        for u in range(1,n+1) : 
            name = input()
            cities.append(name) 
            p = int(input())  
            for _ in range(p) : 
                v,w = map(int,input().split()) 
                graph[u].append((v,w)) 


        Q = int(input()) 

        for _ in range(Q) : 
            name1,name2 = input().split() 
            # get index of the name  
            s = cities.index(name1) + 1 
            f = cities.index(name2) + 1  
    
            print(Dijkstra(s,f))  



