def Sereja_and_Dima() : 

    n = int(input())

    a = list(map(int,input().split()))
    b = []
    player1 = 0 
    player2 = 0
    turn = 1   
    i = 0 
    j = n-1 
    while i <=j : 
        # in case n is odd 
        # s moves first 
        
        if (turn % 2 == 1 ) : # case n = 7
            if (a[i] > a[j])  : 
                player1 += a[i]
                i += 1 
            else : 
                player1 += a[j]
                j -= 1

            turn = turn + 1 

        else :

            if (a[i] > a[j]) : 
                player2 += a[i]
                i += 1 
            else : 
                player2 += a[j]
                j -= 1 

            turn = turn + 1 

    b.append((player1,player2))
    for s in b : 
        print(s[0],s[1])
        exit()

                

            
       
                

print(Sereja_and_Dima())
