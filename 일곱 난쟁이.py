n = 9
tmp1, tmp2 = 0, 0
arr = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            tmp1 = arr[i]
            tmp2 = arr[j]
arr.remove(tmp1)
arr.remove(tmp2)

print("오름차순 정렬:" + '\n' + '\n'.join(map(str, sorted(arr))))