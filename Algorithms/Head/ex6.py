from queue import PriorityQueue 

pq = PriorityQueue() 
def ex6(n) :

    for _ in range(n) : 

        line = int(input().split()) 
    

    if line[0] == '1' : 

        pq.put(line[1]) 
    
    else: 

        if len(pq.queue)//3 == 0 : 
            print('no reviews yet')

        
        else : 
            










if __name__ == '__main__' : 

    n = int(input()) 