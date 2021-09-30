n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
l = r = 0

for i in range(n):
    if a[i] != sorted_a[i]:
        l = i
        break

for i in range(len(a) - 1, -1, -1):
    if a[i] != sorted_a[i]:
        r = i
        break

i, j = l, r
while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

if a != sorted_a:
    print('no') 
    exit()

print('yes')
print('{} {}'.format(l + 1, r + 1))