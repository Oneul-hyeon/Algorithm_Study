import sys
from collections import deque
input = sys.stdin.readline


# 1. 그래프 생성
def bfs(a, b) :
    # 1-1. 큐 생성 후 [시작 노드, 0] 삽입
    queue = deque()
    queue.append((a, 0))
    # 1-2. 거리 리스트 생성 후 시작 위치 업데이트
    distance = [float("inf") for _ in range(n+1)]
    distance[a] = 0
    # 1-3.
    while queue :
        # 1-3-1. 큐에서 노드, 거리 정보 반환
        node, dist = queue.popleft()
        # 1-3-2.
        for next, cost in nodes[node] :
            next_dist = dist+cost
            # 다음 노드까지 가는 거리가 더 짧을 경우
            if next_dist < distance[next] :
                # 거리 정보 업데이트
                distance[next] = next_dist
                # 큐에 [다음 노드, 거리] 삽입
                queue.append((next, next_dist))
    # 1-4. 목표 노드까지의 거리 반환
    return distance[b]

n, m = map(int, input().split())
# 2. 노드 별 연결 노드 리스트 생성
nodes = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a, b, c = map(int, input().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
# 3. 결과 출력
for _ in range(m) :
    a, b = map(int, input().split())
    print(bfs(a, b))