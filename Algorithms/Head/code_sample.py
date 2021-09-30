# function to implement min head algorithm 
def minHeapify(i) : 
    smallest = i
    # position of nodes  
    left = 2*i + 1 
    right = 2*i + 2
    if left < len(h) and h[left] < h[smallest] : 
        smallest = left 
    if right < len(h) and h[right] < h[smallest] : 
         
        smallest = right  # push to font of nodes 

    if smallest != i : 
        h[i] , h[smallest] = h[smallest] , h[i] 
        
        minHeapify(smallest)
# thuc hien chuan hoa cay tu vi tri cuoi cung co node la 
def buildHeap(n) : 
    
    for i in range(n//2-1, -1,-1) :
        minHeapify(i) 
if __name__== '__main__' : 

    h = [7,12,6,10,17,15,2,4] 

    buildHeap(len(h)) 
    
    print(h) 


