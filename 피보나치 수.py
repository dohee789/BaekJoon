# N = int(input())
# arr = [0, 1]
# for i in range(2, N+1):
#     num = arr[i-1] + arr[i-2]
#     arr.append(num)
# print(arr[N])

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))

