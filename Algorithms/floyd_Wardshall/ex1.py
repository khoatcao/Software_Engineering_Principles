INF = 10 ** 9 
def floyd() : 
  for k in range(M) : 
    for i in range(M) : 
      if dist[i][k] == INF : 
        continue
    
      for j in range(M) : 
         if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j] : 
            dist[i][j] = dist[i][k] + dist[k][j] 
            
     
     
'''
if __name__ == '__main__' : 

  V = int(input())
  
  for _ in range(V) : 
    s = input() 
    M = len(s) 
    dist = [[INF] * M for _ in range(M)] 
    matrix = []
    for i in range(M) :
      if i == 0 : 
        matrix.append(s) 
      else : 
        matrix.append(input()) 
        
      for j in range(M)  : 
        
        if matrix[i][j] == 'Y' : 
          dist[i][j] = 1 
        elif i == j :
          dist[i][j] = 0 
      
    floyd() 
    max_friends = 0 
    id = 0 
    
    for i in range(M) : 
      count = 0 
      for j in range(M)  : 
        if dist[i][j] == 2 : 
          count += 1 
      if max_friends > count : 
        max_friends = count 
        id = i 
        
    print(id,max_friends) 

'''
T = int(input())

for _ in range(T):
    s = input()
    M = len(s)
    dist = [[INF] * M for i in range(M)]
    matrix = []

    for i in range(M):
        if i == 0:
            matrix.append(s)
        else:
            matrix.append(input())

        for j in range(M):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0
    
    floyd()
    nfriends, index = 0, 0

    for i in range(M):
        count = 0
        
        for j in range(M):
            if dist[i][j] == 2:
                count += 1
        
        if count > nfriends:
            nfriends = count
            index = i
    
    print(index, nfriends)