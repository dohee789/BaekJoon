N, K = map(int, input().split())
scheduling = list(map(int, input().split()))
# 2 7
# 2 3 2 3 1 2 7
adaptor = [0] * N
count = 0
scheduling_idx = 0
tmp = 0
tmp_i = 0

for i in scheduling:
    # 멀티탭에 같은 전기용품이 있을 때
    if i in adaptor:
        pass
        #print(adaptor,'=')
    # 멀티탭이 아직 채워지지 않았을 때
    elif 0 in adaptor:
        adaptor[adaptor.index(0)] = i
        #print(adaptor,'!=')
    # 멀티탭에 빈자리 없고 현재 꽂혀 있는 전기용품들과 다를 때
    else:
        for j in adaptor:
            #print(j,'%')
            # 현재 꽂혀있는 전기용품이 더 이상 사용되지 않는다면
            if j not in scheduling[scheduling_idx:]:
                #print('--',scheduling[scheduling_idx:])
                tmp = j
                #print(tmp, '?')
                #print(adaptor,'@')
                break
            # 현재 꽂혀있는 전기용품이 이후에도 사용될 때
            # 꽂혀있는 것들 중 여러 개가 다시 사용될 때, 더 나중에 사용되는 것을 뽑는다.
            elif scheduling[scheduling_idx:].index(j) > tmp_i:  
                tmp = j
                #print(tmp, '!')
                tmp_i = scheduling[scheduling_idx:].index(j)
                #print('++',scheduling[scheduling_idx:])
                #print(tmp_i)
                #print(adaptor,'#')
        #print(adaptor,'$$')
        adaptor[adaptor.index(tmp)] = i
        #print(i, '_')
        #print(tmp, '&')
        #print(adaptor,'~~')
        tmp = tmp_i = 0
        count += 1
    scheduling_idx += 1

print(count)