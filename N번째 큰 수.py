import sys
T = int(input())
for _ in range(T):
    A = list(map(int, sys.stdin.readline().strip().split()))
    A.sort()
    #A = sorted(map(int, sys.stdin.readline().strip().split()))
    print(A[-3])