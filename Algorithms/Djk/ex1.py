from queue import PriorityQueue

MAX = 100 
INF = int(1e9) 

class Node : 
    # id la vertices 
    # dist is cost 
    def __init__(self,id,dist) :
        self.dist = dist 
        self.id = id 

    def __lt__(self,other) : 

        return self.dist <= other.dist 
# djk implementation 
def ex1(s) : 

    # data preparation 
    pq = PriorityQueue() 
    pq.put(Node(s,0)) 
    dist[s] = 0 
    
    while pq.empty() == False : s 
        top = pq.get() 
        u  = top.id 
        w = top.dist 
        # xet dinh ke voi u 
        for neighbor in graph[u] : 

            if w + neighbor.dist < dist[neighbor.id] :

                dist[neighbor.id] = w + neighbor.dist 
                 
                pq.put(Node(neighbor.id,dist[neighbor.id]))

                path[neighbor.id] = u # luu
# main function 

if __name__ == '__main__' : 

    n = int(input())
    graph = [[] for _ in range(n+5)] 
    dist = [INF for _ in range(n+5)] 
    path = [-1 for _ in range(n+5)] 
    
    for i in range(n) : 
        a,b,w  = map(int,input().split())
        
        graph[a].append(Node(b,w)) 
        graph[b].append(Node(a,w)) 

    

    s = int(input()) 

    ex1(s) 

    Q = int(input()) 

    for _ in range(Q) : 

        v = int(input()) 

        print(dist[v] if dist[v] != INF else 'no path') 