import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 1. 다익스트라 함수 생성
def dijkstra(start) :
    # 1-1. 힙 생성 후 (0, 0, 1) 삽입
    heap = []
    heappush(heap, (0, 0, 1))
    # 1-2, 현재 노드 거리 정보 업데이트
    information[1] = [0, 0]
    # 1-3.
    while heap :
        # 1-3-1. 힙에서 정보 반환
        now_m, now_t, node = heappop(heap)
        # 1-3-2. 이미 처리가 된 경우 continue
        if information[node][0] < now_m and information[node][1] < now_t : continue
        # 1-3-3.
        for next, time, cost in graph[node] :
            # 돈, 시간 계산
            next_m, next_t = now_m + cost, now_t + time
            # 시간 또는 돈이 초과할 경우 continue
            if next_m > m or next_t > t : continue
            # 돈 또는 시간이 하나라도 많이 남을 경우
            if next_m < information[next][0] or next_t < information[next][1] :
                # 시간이 절약될 경우
                if next_m < information[next][0] or (next_m == information[next][0] and next_t < information[next][1]): information[next] = [next_m, next_t]
            # 힙에 정보 삽입
            heappush(heap, (next_m, next_t, next))

n = int(input())
t, m = map(int, input().split())
l = int(input())

# 2. 그래프 생성 후 업데이트
graph = [[] for _ in range(n+1)]
for _ in range(l) :
    a, b, time, cost = map(int, input().split())
    graph[a].append((b, time, cost))
    graph[b].append((a, time, cost))
# 3. 시간-돈 정보 리스트 생성
INF = float("inf")
information = [[INF, INF] for _ in range(n+1)]
# 4. 다익스트라 실행
dijkstra(1)
# 5. 결과 출력
print(information[-1][0] if information[-1][0] != INF else -1)
