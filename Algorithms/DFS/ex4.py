def dfs(src) :   
  global answer 
  flag[src] = True 
  visited[src] = True 
  for v in graph[u] : 
      if (flag[v]) : 
        answer = "YES"
        return answer  
      if (visited[v]) : 
        continue
        
      dfs(v) 
  flag[src] = False  
if __name__=='__main__' : 
  T = int(input())
  for _ in range(T) :
     N,M  = map(int,input().split())
     max = N + 5 
     flag = [False] * max 
     visited = [False] * max
     graph = [[] for _ in range(max)]  
     for _ in range(M) :      
        u,v = map(int,input().split()) 
        graph[u].append(v)
        graph[v].append(u)
     answer = 'N0' 
     for i in range(N) : 
        if (visited[i] == False) : 
          dfs(i)
          
     print(answer,'\n') 
       
        
      
      
      
    
      
      
  
