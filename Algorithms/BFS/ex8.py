from queue import Queue
MAX = 100000 + 5  
dr = [0,0,1,-1] 
dc = [1,-1,0,0] 
backyard = [0 for _ in range(MAX)]
nsheep = nwolf = 0 
def bfs(i,j) :
    global nsheep, nwolf 
    q = Queue() 

    q.put((i,j)) 
    sheep = (1 if backyard[i][j] == 'k' else 0) 
    wolf  = (1 if backyard[i][j] == 'v' else 0 ) 
    connectedOutside = False # out of backyard preserve the quantity of wolfs and sheeps 

    backyard[i][j] = '#' 
    while not q.empty() : 
        x, y = q.get()  

        for i in range(4) : 

            u = x + dr[i] 
            v = y + dc[i] 

            # check if outside the backyard 

            if not ( u in range(n) and v in range(m)) : 

                connectedOutside = True 
                continue 
                
            if backyard[u][v] !=  '#' : 
                sheep += ( 1 if backyard[u][v] == 'k' else  0)
                wolf += ( 1 if backyard[u][v] == 'v' else 0 )
                backyard[u][v] = '#' 
                q.put((u,v)) 


    if connectedOutside : 
        nsheep  += sheep 
        nwolf += wolf 
    else : 
        if sheep > wolf : 
            nsheep += sheep 

        else : 
            nwolf += wolf 
    
    return nsheep,nwolf 


# reading input 

line = '' 

while line == '' :
    line = input().strip() 

n,m = map(int,line.split()) 

for  i in range(n) : 
    backyard[i] = list(input()) 

for i in range(n) : 
    for j in range(m) : 
        if backyard[i][j] != '#': 
            bfs(i,j) 

print(nsheep,nwolf)  