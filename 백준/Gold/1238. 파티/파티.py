import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# 1. 다익스트라 함수 정의
def dijkstra(start) :
    # 1-1. 시간 리스트 생성
    time = [float("INF") for _ in range(n+1)]
    # 1-2. 힙 생성 후 (0, 출발 노드) 삽입
    heap = []
    heappush(heap, (0, start))
    # 1-3. 현재 노드 시간 정보 업데이트
    time[start] = 0
    # 1-4.
    while heap :
        # 1-4-1. 힙에서 정보 반환
        cost, node = heappop(heap)
        # 1-4-2. 이미 처리된 경우 continue
        if time[node] < cost : continue
        # 1-4-3.
        for next, t in graph[node] :
            # 다음 노드로 가는 시간 계산
            next_t = cost + t
            # 계산된 시간이 더 적게 걸리는 경우
            if time[next] > next_t :
                # 시간 정보 업데이트
                time[next] = next_t
                # 힙에 (업데이트된 시간, 노드) 삽입
                heappush(heap, (next_t, next))
    # 1-5. 시간 리스트 반환
    return time

n, m, x = map(int, input().split())

# 2. 학생 별 총 소요 시간 리스트 생성
student = [0 for _ in range(n+1)]
# 3. 그래프 생성 후 간선 정보 입력
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
# 4.
for i in range(1, n+1) :
    if i == x : continue
    # 4-1. 각 노드 -> X번 마을로 향하는 시간 업데이트
    student[i] += dijkstra(i)[x]
# 5. 다익스트라를 실행해 X 번 마을에서 각 노드로 향하는 시간 구하기
x2node = dijkstra(x)
# 6. 시간 정보 업데이트
for i in range(1, n+1) :
    student[i] += x2node[i]
# 7. 결과 출력
print(max(student))
