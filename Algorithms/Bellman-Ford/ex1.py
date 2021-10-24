INF = 10 ** 9
MAX = 2005  
class Edge : 
    def __init__(self,_source,_target,_weight) : 

        self.source = _source 
        self.target = _target 
        self.weight = _weight 

    

# data preparation 

dist = [INF for _ in range(MAX)]
graph = [] 

def Bellman_ford(s) : 

    dist[s] = 0 

    for i in range(n-1): 

        for j in range(m)  : 

            u = graph[j].source 
            v = graph[j].target 
            w = graph[j].weight 

            if (dist[u] != INF ) and (dist[u] + w < dist[v]) : 
                dist[v] = dist[u] + w 
        
    for i in range(m) : 

            u = graph[i].source 
            v = graph[i].target 
            w = graph[i].weight 

            if (dist[u] != INF ) and (dist[u] + w < dist[v]) : 
                return False
        
    return True 


if __name__ == '__main__' : 

    T = int(input())
    for _ in range(T) : 
        n,m = map(int,input().split()) 

        for _ in range(m) :  
            u,v,w = map(int,input().split()) 
            graph.append(Edge(u,v,w))


 
        print("possible" if not Bellman_ford(0) else "not possible")  



    



