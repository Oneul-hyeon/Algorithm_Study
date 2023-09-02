import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 1. 다익스트라 함수 정의
def dijkstra(start) :
    # 1-1. 힙에 (0, 출발점) 삽입
    heap = []
    heappush(heap, (0, start))
    # 1-2. 현재 위치에 만나는 소의 수 입력
    caws[start] = 0
    # 1-3.
    while heap :
        # 1-3-1. 힙에서 (만나는 소의 수, 노드) 반환
        caw, node = heappop(heap)
        # 1-3-2. 해당 노드에 저장되어 있는 소의 수보다 만나는 소의 수가 클 경우 continue
        if caws[node] < caw : continue
        # 1-3-3.
        for info in graph[node] :
            # 비용 계산
            cost = caw + info[1]
            # 비용이 다음 노드에 저장된 값보다 작을 경우
            if cost < caws[info[0]] :
                # 만나는 소의 수 업데이트
                caws[info[0]] = cost
                # 힙에 (소의 수, 노드) 삽입
                heappush(heap, (cost, info[0]))

n, m = map(int, input().split())
# 2. 다익스트라를 위한 배열 생성
graph = [[] for _ in range(n+1)]
# 3. 만나는 소들의 수 리스트 생성
caws = [float('inf')] * (n+1)
# 4. 간선 정보 입력
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
# 5. 다익스트라 실행
dijkstra(1)
# 6. 결과 출력
print(caws[n])