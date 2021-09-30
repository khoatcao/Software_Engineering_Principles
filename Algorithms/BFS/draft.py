from queue import Queue 
MAX = 8 + 5 
graph = [[] for _ in range(MAX)]
visited = [False] * MAX
nsheep = nwolf = 0 # the quantity of sheeps and wolf of traversing with bfs 
dr = [0,0,-1,1] 
dc = [-1,1,0,0] 
fence_backyard = [0 for _ in range(MAX)]
# i,j la toa do cua dinh ke i,j 
def bfs(i,j) : 
    global nsheep,nwolf 
    q = Queue() 
    q.put((i,j)) 
   # count outside backyard
    sheep = (1 if fence_backyard[i][j] == 'k' else 0) 
    wolf  = (1 if fence_backyard[i][j] == 'v' else 0) 
    connected_outside = False 
    fence_backyard[i][j] = '#'
    while not q.empty() : 
      (x,y) = q.get()
      # xet dinh ke cua u va v 
      # pair (u,v) 
      for i in range(4) : 
        u = x + dr[i] 
        v = y + dc[i]
        
        if not (u in range(n) and v in range(m)) : 
          connected_outside = True 
          continue 
        
        if fence_backyard[u][v] != '#' : 
          sheep += (1 if fence_backyard[u][v] == 'k' else 0) 
          wolf  += (1 if fence_backyard[u][v] == 'v' else 0)
          fence_backyard[u][v] = '#' 
          q.put((u,v))
    if connected_outside : 
      nsheep += sheep 
      nwolf += wolf 
    else : 
      if sheep > wolf : 
        nsheep += sheep 
      else : 
        nwolf += wolf 





line = '' 
while line == '' : 
  line = input().strip() 
n,m = map(int,line.split())  
for i in range(n) : 
  fence_backyard[i] = list(input()) 

for i in range(n) : 
  for j in range(m) : 
    if fence_backyard[i][j] != '#': 
      bfs(i,j) 
      
print(nsheep,nwolf) 
