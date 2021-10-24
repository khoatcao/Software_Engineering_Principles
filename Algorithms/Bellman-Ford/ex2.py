
INF = 10 ** 9 

MAX = 200 + 5 

dist = [INF for _ in range(MAX )] 

class Edge : 

    def __init__(self,_source,_target,_weight) : 

        self.source = _source 
        self.target = _target 
        self.weight = _weight 


    


def Bellman_Ford(s) :

    dist[s] = 0 

    for i in range(n-1) : 

        for j in range(m) : 
            u = graph[j].source 
            v = graph[j].target 
            w = graph[j].weight 

            if (dist[u] != INF ) and (dist[u] + w < dist[v]) : 
                dist[v] = dist[u] + w 


    for i in range(n-1) :     
        for j in range(m) : 

         u = graph[j].source 
         v = graph[j].target 
         w = graph[j].weight 

         if (dist[u] != INF ) and (dist[u] + w < dist[v]) : 
            dist[v] = -INF   

if __name__ == '__main__' : 

    T = int(input()) 

    for t in range(1,T+1)  :
        input() 
        n = int(input()) # the number of conjuntion 

        weight = [0] + list(map(int,input().split()))

        m = int(input()) 
        graph = [] 
        for _ in range(m) : 

            u,v = map(int,input().split()) 
            graph.append(Edge(u,v,(weight[v] - weight[u])**3)) 

        
        Bellman_Ford(1) 
        Q = int(input())

        print("Case {} :".format(t))

        for _ in range(Q) : 

            f = int(input()) 

            print(dist[f] if dist[f] != INF and dist[f] >= 3 else "?")  





        