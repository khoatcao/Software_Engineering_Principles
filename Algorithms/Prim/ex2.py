from queue import PriorityQueue 
from math import sqrt 
MAX = 10000 + 5 
INF = 1e9

class Scanner : 

    def __generator__() : 

        while True : 

            try :

                buff = input().strip().split() 

                for x in buff : 

                    yield x 


            except EOFError : 

                exit()

    sc = __generator__()  

    def next() : 

        return Scanner.sc.__next__() 

class Node : 

    def __init__(self,_id,_dist) : 

        self.id = _id 

        self.dist = _dist 

    
    def __lt__(self,other) : 

        return self.dist <= other.dist 


def primmst() :

    ans = 0 

    for i in range(n) : 

        if path[i] == -1 : 

            continue 

        ans += dist[i] 

    return ans  



def prim(graph,s) : 

    pq = PriorityQueue() 
    pq.put(Node(0,s))
    dist[s] = 0 

    while pq.empty() == False : 

        u = pq.get().id 
        visited[u] = True 

        for v in range(n) : 
           if visited[v] == False and graph[u][v] < dist[v] : 

            dist[v] = graph[u][v] # weight = graph[u][v] 

            pq.put(Node(v,dist[v]))
            
            path[v] = u 
            

# function to calculate the distance in space 
def distance(x1,y1,x2,y2) :

    d= (x1 - x2)**2 + (y1- y2)**2 

    return sqrt(d) 




if __name__ == '__main__' : 

    while True : 

        n = int(Scanner.next()) 

        dist = [INF ] * n 

        path = [-1] * n 

        visited = [False] * n 


        x = [0] * n 
        y = [0] * n 

        for i in range(n) : 

            x[i],y[i] = int(Scanner.next()),int(Scanner.next()) 


        graph = [] 

        for i in range(n) : 

            graph.append([]) 

            for j in range(n) : 
                graph[i].append(distance(x[i],y[i],x[j],y[j])) 

        
        m = int(input()) 

        for i in range(m) :
            u,v = int(Scanner.next()) , int(Scanner.next()) 

            u -= 1 

            v -= 1 

            graph[u][v] = 0 

            graph[v][u] = 0 

        
        prim(graph,0) 
        print("%.2f" % primmst()) 

