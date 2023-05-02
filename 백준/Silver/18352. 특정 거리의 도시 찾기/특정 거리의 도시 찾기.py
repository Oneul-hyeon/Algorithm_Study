import sys, math, heapq
input = sys.stdin.readline

INF = math.inf

n, m, k, x = map(int, input().split())
# 1. n+1개의 인자를 갖는 리스트 생성
graph = [[] for _ in range(n+1)]
# 2. 최단거리 리스트 생성
distance = [INF for _ in range(n+1)]

# 3. 모든 간선의 정보 입력받기
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append((b, 1))

# 4. 다익스트라 재귀 함수 생성
def dijkstra(start) :
    # 5. 힙에 사용할 리스트 선언
    heap = []
    # 6. 리스트에 (0, start) push
    heapq.heappush(heap, (0, start))
    # 7. 시작 지점 거리 지정
    distance[start] = 0
    while heap :
        # 9. 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(heap)
        # 10. 현재 노드가 이미 처리된 적 있다면 무시
        if dist < distance[now] : continue
        # 11. 현재 노드와 연결된 인접 노드 확인
        for i in graph[now] :
            # 11-1. 비용 계산
            cost = dist + i[1]
            # 11-2. 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

# 12. 다익스트라 알고리즘 수행
dijkstra(x)

# 13. 최단 거리가 k인 도시 출력
if k not in distance : print(-1)
else :
    for i in range(n+1) :
        if distance[i] == k : print(i)
