INF = 10 ** 9 
MAX = 105 

class Edge : 

    def __init__(self,_source,_target,_weight) : 

        self.source = _source 
        self.target = _target 
        self.weight = _weight 
dist = [INF for _ in range(MAX)] 
path = [-1 for _ in range(MAX)] 
graph = [] 
def BellmanFord(s) : 

    # gan chi phi = 0 
    dist[s] = 0 

    for i in range(1,n) : 
        for j in range(m) : 

            u = graph[j].source 
            v = graph[j].target
            w = graph[j].weight 
        
            if (dist[u] != INF) and (dist[u] + w  < dist[v]) : 

                dist[v] = dist[u] + w 
                path[v] = u 
    # loop for m round if graph contains negative cycles 
    for i in range(m) : 
        u = graph[i].source 
        v = graph[i].target 
        w = graph[i].weight 

        if (dist[u] != INF ) and (dist[u] + w < dist[v]) : 
            return False 

    return True # graph only contain positive cycles 

if __name__ == '__main__' : 

    n,m = map(int,input().split()) 

    for i in range(m) : 
        u,v,w = map(int,input().split()) 
        graph.append(Edge(u,v,w)) 
    
    s,t = 0,4 

    res = BellmanFord(s) 
    

    if not res :

        print("Graph contains negative weight cycle")  


    else : 
        print(dist[t])      