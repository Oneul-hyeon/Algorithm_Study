from heapq import heappush, heappop
def solution(n, vertex):
    # 1. 다익스트라 함수 정의
    def dijkstra(start) :
        # 1-1. 힙 생성 후 (거리, 출발 노드) 삽입
        heap = []
        heappush(heap, (0, start))
        # 1-2. 거리 정보 업데이트
        distance[start] = 0
        # 1-3.
        while heap :
            # 1-3-1. 힙에서 정보 추출
            d, node = heappop(heap)
            # 1-3-2. 이미 처리된 경우 continue
            if d > distance[node] : continue
            # 1-3-3.
            for next, c in graph[node] :
                # 거리 계산
                cost = d + c
                # 다음 노드에 도달하는 거리보다 짫을 경우
                if distance[next] > cost :
                    # 거리 정보 업데이트
                    distance[next] = cost
                    # 힙에 정보 삽입
                    heappush(heap, (cost, next))
        
    # 2. 그래프 생성 후 간선 정보 입력
    graph = [[] for _ in range(n+1)]
    for a, b in vertex :
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    # 3. 거리 정보 리스트 생성
    distance = [float('inf') for _ in range(n+1)]
    # 4. 다익스트라 실행
    dijkstra(1)
    # 5. 결과 리턴
    return distance[1:].count(max(distance[1:]))
