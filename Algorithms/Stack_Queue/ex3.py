def Cards_Throwing() : 

    while True : 

        n = int(input())

        if n == 0 : 
            break 

import queue 

def card_throwing() : 

    while True : 
        deck = queue.Queue() 
        n = int(input())

        if n == 0 : 
            break 


        for i in range(1,n+1) : 
            # add values to queue    
            deck.put(i) 


        Discarded_cards = [] 

        while deck.qsize() >= 2 :

            Discarded_cards.append(deck.get())
            # adding top the the bottom of the queue 
            deck.put(deck.get()) 
        


        print('Discarded cards' if Discarded_cards else 'Discarded cards' ,end = '') 
        print(*Discarded_cards, sep =  ', ') 
        print('Remaining card', deck.get()) 

result = card_throwing()
result 