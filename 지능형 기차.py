import sys
passenger = 0
max_passenger = 0

for _ in range(10):
    #out_p, in_p = map(int, input().split())
    out_p, in_p = map(int, sys.stdin.readline().strip().split())
    passenger += in_p - out_p
    max_passenger = max(passenger, max_passenger) 
print(max_passenger)
