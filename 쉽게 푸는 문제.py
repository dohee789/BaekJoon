x, y = map(int, input().split())
a = []
for i in range(y+1) :
    for j in range(i):
        if len(a) == y:
            break
        a.append(i)
print(a)
print(sum(a[x-1:y]))