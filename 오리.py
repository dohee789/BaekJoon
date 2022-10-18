import sys
#input = sys.stdin.readline

dic = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}
duck = input()

answer = 0
queue = []
for i in duck:
    flag = True
    for j in range(len(queue)):
        # 입력값+1과 dic의 value값을 비교하여 같다면 큐를 갱신
        # 문자열의 길이는 5의 배수여야함
        if(queue[j]+1)%5 == dic[i]:
            queue[j] = (queue[j]+1)%5
            flag = False
            break
    # 시작은 True
    if flag:
        # 처음 시작이 q여야 시작
        if dic[i] != 0:
            answer = -1
            break
        queue.append(0)

if answer == -1:
    print(-1)
else:
    for num in queue:
        # 4가 아닐경우는 k로 끝나지 않았다는것
        if num != 4:
            print(-1)
            break
    else:
        print(len(queue))
