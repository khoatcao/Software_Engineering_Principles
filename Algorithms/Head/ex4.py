from queue import PriorityQueue 


class Topic : 

    def __init__(self,_id,_old_score,_new_score) : 

        self.id = _id 
        self.old_score = _old_score  
        self.new_score = _new_score 

        self.change = self.new_score - self.old_score 

    
    # comparision sepcial method 
    def __lt__(self,other) : 

        return self.change > other.change or (self.change == other.change and self.id > other.id) 

    


pq = PriorityQueue() 

def ex4(n) : 

    for _ in range(n) : 
        id,old_score,post,like,comment,share = map(int,input().split()) 
        
        new_score = post * 50 + like * 5 + comment * 10 + share * 20 

        pq.put(Topic(id,old_score,new_score)) 

    for _ in range(5) : 
        t = pq.get() 

        print(t.id,t.new_score) 
if __name__ == '__main__' : 

    n = int(input()) 
    ex4(n) 
