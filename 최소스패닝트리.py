import sys
input = sys.stdin.readline

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
# 부모 테이블 초기화하기(리스트 = list(range(횟수)))
parent = list(range(v + 1)) 

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
		# 튜플은 원소가 여러개일때 첫번째 원소를 기준으로 정렬수행
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선을 하나씩 확인하며
for cost, a, b in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함시키고 비용을 더해줌
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)