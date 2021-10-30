from queue import PriorityQueue 

MAX = 50 + 5 
INF = 1e9 
class Node : 

    def __init__(self,_id,_dist) : 
        self.dist = _dist 
        self.id = _id 
    
    def __lt__(self,other) : 

        return self.dist <= other.dist 




def prim(graph,s) : 

    n = len(graph) 
    dist = [INF ] * n 
    path = [-1] * n 
    visited = [False] * n 
    pq = PriorityQueue() 
    pq.put(Node(s,0)) 
    dist[s] = 0 
    total_cost = 0 
    while pq.empty() == False : 

        u = pq.get().id

        visited[u] = True 

        for neighbor in graph[u] : 

            w = neighbor.dist 
            v = neighbor.id 

            if visited[v] == False and w < dist[v] : 
                dist[v] = w 

                pq.put(Node(v,w)) 
                path[v] = u 


    for i in range(n) :
            
        if dist[i] >= INF : 

            return 'Impossible' 
        
        total_cost += dist[i] 

    return total_cost 
        




if __name__ == '__main__' : 


    test = int(input()) 

    for t in range(test) : 

        input() 

        m = int(input()) 
        graph = []
        index = 0  
        cities = dict() 

        for _ in range(m) : 
 
            name1,name2,cost = input().split() 

            if name1 in cities : 
                u = cities[name1]

            else : 
                u = index 
                cities[name1] = index 
                graph.append([]) 
                index += 1 

            
            if name2 in cities : 

                v = cities[name2] 

            else : 

                v = index 
                cities[name2] = index 

                graph.append([]) 
                index += 1
            cost = int(cost)
            graph[u].append(Node(v,cost)) 
            graph[v].append(Node(u,cost)) 

            print("Case {} : {}".format(t+1,prim(graph,0)))


            





            
            





    


