INF = 10 ** 9 
MAX = 28 
def floyd(dist) : 
  
  for k in range(MAX) :
    for u in range(MAX) : 
      for v in range(MAX) : 
        # k is an intermidiate note 
        dist[u][v] = min(dist[u][v],dist[u][k] + dist[k][v])
        
# main function 
if __name__ == '__main__' :
  
  while True : 
    n = int(input())
    
    if n == 0 : 
      break 
    # init dist for young and people older than 30
    distS = [[0 if  i == j else INF for i in range(MAX)] for j in range(MAX)] # array for yong 
    distT = [[0 if i == j else INF for i in range(MAX )] for j in range(MAX)] # array for people than 30 or older 
    for _ in range(n) : 
      type,direction,x,y,c = input().split()
      u,v = map(lambda char:ord(char) - ord('A'), (x,y))
      c = int(c) 
      if type == 'Y': 
        distS[u][v] = min(distS[u][v],c) 
        if direction == 'B' : # bidirectional path 
          distS[v][u] = min(distS[v][u],c) 
          
      else : # for people more than 30 
        distT[u][v] = min(distT[u][v],c) 	
        if direction == 'U' : 
          distT[v][u] = min(distT[v][u],c) 
      
    S,T = map(lambda char : ord(char) - ord('A'),input().split())
    floyd(distS)
    floyd(distT) 
      
    Total_energy = INF 
    cities = [] 
    for u in range(MAX) : 
        if distS[S][u] != INF and distT[T][u] != INF : 
          E = distS[S][u] + distT[T][u]
          if E == Total_energy : 
            city = chr(u + ord('A')) 
            cities.append(city) 
            
          if E < Total_energy : 
            Total_energy = E 
            city = chr(u + ord('A')) 
            cities = [city]
            
            
            
        if Total_energy == INF : 
          print("You will never meet.") 
          
        else : 
          for city in cities : 
            print(Total_energy,city) 
            
      
      
      
          
          
      
      
      
  
        
        