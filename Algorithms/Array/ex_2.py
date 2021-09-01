def museum_solution() : 

    n = input()

    # count sum 
    s = 0 
    cur = 'a'
    for i in n : 
        print(i)
        s += min((26 - abs(ord(cur) - ord(i))), abs(ord(cur) - ord(i)))
        cur = i       
        
    return s        
        
        
print(museum_solution()) 