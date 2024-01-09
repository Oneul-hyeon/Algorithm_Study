import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 1. 다익스트라 함수 정의
def dijkstra(start) :
    # 1-1. 거리 정보 리스트 생성
    distance = [INF for _ in range(n+1)]
    # 1-2. 현재 위치 거리 정보 입력
    distance[start] = 0
    # 1-3. 힙 생성 후 (0, 현재 위치) 삽입
    heap = []
    heappush(heap, (0, start))
    # 1-4.
    while heap :
        # 1-4-1. 거리, 노드 정보 반환
        dist, now = heappop(heap)
        # 1-4-2. 이미 처리된 경우 continue
        if distance[now] < dist : continue
        # 1-4-3.
        for next, cost in graph[now] :
            # 다음 노드까지 가는 거리 계산
            next_cost = dist + cost
            # 계산된 거리가 더 짧을 경우
            if next_cost < distance[next] :
                # 거리 정보 업데이트
                distance[next] = next_cost
                # 힙에 (업데이트된 거리, 노드) 삽입
                heappush(heap, (next_cost, next))
    # 1-5. 거리 정보 반환
    return distance

n, e = map(int, input().split())
INF = float("INF")
# 2. 그래프 생성 후 간선 정보 입력
graph = [[] for _ in range(n+1)]
for _ in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
u, v = map(int, input().split())
# 3. 다익스트라를 통해 시작지점으로부터의 거리 정보, u-v간 거리 정보, 도착지점으로부터의 거리 정보 생성
start, mid, end = dijkstra(1), dijkstra(u), dijkstra(n)
# 4. 경로가 존재하지 않을 경우 -1 출력
# 5. 이외의 경우 최소 거리 출력
case1 = start[u] + mid[v] + end[v]
case2 = start[v] + mid[v] + end[u]
print(-1 if case1 == case2 == INF else min(case1, case2))
