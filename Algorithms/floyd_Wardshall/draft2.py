INF = 9999 
def printpath(path,s,f) : 

    if s == f : 

        print(f,end = ' ')
        return 

    if path[s][f] == -1 : 
        print("no path",end  = '')

    printpath(path,s,path[s][f]) 
    print(f,end = ' ') 

def printsolution(graph,dist,v) : 

    for i in range(v) : 
        for j in range(v) : 
            if i != j : 
                print('--------------------\n{} -> {}'.format(i,j) + ":") 

                printpath(path,i,j) 
                print() 

                if path[i][j] != -1 : 
                    print('Total length {}'.format(dist[i][j]))
def FloydWardshall(graph,dist,path,v) : 
    for i in range(v) : 
        for j in range(v) : 
            dist[i][j] = graph[i][j] 

            if graph[i][j]  != INF and i != j : 
                path[i][j] = i 

            else : 
                path[i][j] = -1 
    for k in range(v) : 

        for i in range(v) : 

            if dist[i][k] == INF : 
                continue 

            for j in range(v) : 
                
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j] : 
                    dist[i][j] = dist[i][k] + dist[k][j] 

                    path[i][j] = path[k][j] 


    for i in range(v) : 
            if dist[i][i] < 0 : 
                return False 

        
    return True 





v = int(input()) 

graph = [[ None for _ in range(v)] for j in range(v)]

dist = [[ None for i in range(v)] for j in range(v)] 

path = [[ None for _ in range(v)] for j in range(v)]


for i in range(v) : 
    line = list(map(int,input().split()))

    for j in range(v) : 
        graph[i][j] = INF  if line[j] == 0 and i != j else line[j] 


if FloydWardshall(graph,dist,path,v) : 
    printsolution(path,dist,v) 

else : 
    print("Graph contains negative cycles")
