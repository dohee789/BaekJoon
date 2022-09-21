import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))
sosu = 0
for i in arr:
    cnt = 0
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                cnt += 1
        if(cnt == 1):
            sosu += 1
print(sosu)
