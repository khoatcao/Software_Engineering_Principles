def street_parade() : 
    while True :
        n = int(input()) 
        if n == 0 : 
            break 
        else : 
            c = list(map(int,input().split()))
            i = 0 
            ordering = 1 # to save the order of the truck 
            side_street = [] # save abtrary order

            while i < n : 

               if c[i] == ordering : 
                 ordering += 1 
                 i += 1 

        
               elif  len(side_street) > 0    and side_street[-1] == ordering : 
                  ordering +=1 
                  side_street.pop()
        

               else : 
                  side_street.append(c[i])
                  i+= 1 
 
        
            while len(side_street) > 0  and side_street[-1] == ordering : 
                  ordering += 1 
                  side_street.pop() 

    
            if ordering == n + 1 : 
                print('\nyes')
            else 
                print('\nno ')

#n = int(input())
#c = list(map(int,input().split()))

#zero = int(input())

result = street_parade() 

result 