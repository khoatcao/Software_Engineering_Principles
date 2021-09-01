def bear_and_game() : 
    n = input() 
    l = list(map(int,input().split()))
    # mins to start the game 
    cur = 0 
    min = 0 
    for i in range(len(l)) :
        # greater than 15 
        
            if l[i]- cur > 15 : 
                # n = 1 has one value  
                if i == 0 :
                    min = 0 + 15 # number 16  
                else : # 7 20 88 
                    min = cur + 15
                    cur = l[i] 
                break 
                
    
            else : # < 15 
                if i == (len(l) - 1) : 
                    if (l[i] + 15) >= 90 : 
                        min = 90 
                    else : 
                        min = l[i] + 15 
                else : 
                    min = l[i] 
            cur = l[i]
    
    return min 

print(bear_and_game())



        

print(bear_and_game())
        
        