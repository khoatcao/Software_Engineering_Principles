def binary_search(a,left,right,x) : 
  while left <= right : 
    
    mid = (left + right)//2 
    
    if x == a[mid] : 
      return True 
    elif x < a[mid] : 
      right = mid - 1 
    else : 
      left = mid + 1 
  return False
  
if __name__ == '__main__' : 
  t = int(input()) 
  for _ in range(t) : 
    n,m = map(int,input().split()) 
    a  = list(map(int,input().split()))
    a.sort()
    count = 0 
    for i in range(n) : 
      comp = m - a[i]
      if binary_search(a,i+1,n-1,comp) : 
        count += 1 
        
    print(count)
      
      
      
 

