import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution(n, m) :
    # 1. 다익스트라 함수 생성
    def dijkstra(node) :
        # 1-1. 힙 리스트를 생성해 (거리, 노드) 정보 삽입
        heap = []
        heappush(heap, (0, node))
        # 1-2. 거리 정보 리스트 업데이트
        distance[node] = 0
        # 1-3.
        while heap :
            # 1-3-1. 거리, 노드 정보 반환
            d, n = heappop(heap)
            # 1-3-2. 이미 처리된 경우 continue
            if distance[n] < d : continue
            # 1-3-3.
            for i in graph[n] :
                cost = d + i[1]
                # 현재 노드를 거쳐 다른 노드로 가는 게 더 짧을 경우
                if cost < distance[i[0]] :
                    # 힙에 (비용, 노드) 삽입
                    heappush(heap, (cost, i[0]))
                    # 거리 정보 업데이트
                    distance[i[0]] = cost
    # 2. 거리 정보 리스트 생성
    graph = [[] for _ in range(n+1)]
    distance = [int(1e9) for _ in range(n+1)]
    # 3.
    for _ in range(m) :
        a, b, c = map(int, input().split())
        # 간선 정보 업데이트
        graph[a].append((b, c))
        graph[b].append((a, c))
    s, t = map(int, input().split())
    # 4. 다익스트라 실행
    dijkstra(s)
    # 5. 결과 출력
    print(distance[t])

if __name__ == "__main__":
    n, m = map(int, input().split())
    solution(n, m)