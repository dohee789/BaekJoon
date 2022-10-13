# 특정 원소가 속한 집합(루트노드)을 찾기(부모테이블, 현재노드)
def find_parent(parent, x):
    # 현재 부모가 자기자신이 아니라면 즉, 루트 노드가 아니라면, 
    # 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(부모테이블, 노드번호, 노드번호)
def union_parent(parent, a, b):
    # a, b의 루트노드 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은것으로 갱신
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합(루트노드) 출력하기 -> 같은 루트 노드를 가진다면 같은 집한에 속한것
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')