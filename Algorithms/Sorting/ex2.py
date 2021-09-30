def chores(h) : 
    h.sort()

    x = h[b] - h[b-1]
    return x 
n,a,b = list(map(int,input().split()))
h = list(map(int,input().split()))

result = chores(h)
print(result)





    