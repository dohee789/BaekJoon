M = int(input())
N = int(input())
arr = []
for i in range(M, N+1):
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        arr.append(i)
if not arr:
    print(-1)
else:
    print(sum(arr),min(arr))

# if len(arr) > 0:
#     print(sum(arr),min(arr))
# else:
#     print(-1)
