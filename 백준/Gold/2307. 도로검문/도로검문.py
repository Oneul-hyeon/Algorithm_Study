import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution(n, m):
    # 1. 다익스트라 함수 정의
    def dajikstra(start) :
        min_route = []
        # 1-1. 거리 정보 리스트 생성
        distance = [float('inf') for _ in range(n+1)]
        # 1-2. 힙 생성 후 (거리, 현재 노드, 경로) 정보 삽입
        heap = []
        heappush(heap, (0, start, [start]))
        # 1-3. 거리 정보 업데이트
        distance[start] = 0
        # 1-4.
        while heap :
            # 1-4-1. 힙에서 정보 반환
            d, now, route = heappop(heap)
            # 1-4-2. 이미 최소 거리가 처리된 경우 continue
            if distance[now] < d : continue
            # 1-4-3.
            for next, c in graph[now] :
                # 다음 노드로 가는 비용 계산
                next_d = d + c
                # 다음 노드로 가는 거리보다 비용이 적을 경우
                if distance[next] > next_d :
                    # 탈출 도시일 경우 최단 경로 업데이트
                    if next == n :
                        min_route = route + [next]
                    # 거리 정보 업데이트
                    distance[next] = next_d
                    # 힙에 정보 삽입
                    heappush(heap, (next_d, next, route + [next]))
        # 1-5. 최단 시간, 최단 경로 반환
        return distance[n], min_route

    # 2. 그래프 생성 후 간선 정보 입력
    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        graph[b].append((a, t))
    # 3. 최단 시간, 최단 경로 구하기
    min_time, min_route = dajikstra(1)
    # 4. 경로가 없을 경우 -1 출력
    if not min_route : print(-1)
    # 5. 이외의 경우
    else :
        update_max_time = -float('inf')
        # 4-1.
        for i in range(len(min_route) - 1) :
            a, b = min_route[i], min_route[i+1]
            # 경로 제거
            for idx, info in enumerate(graph[a]) :
                if info[0] == b :
                    info_a = info[:]
                    del graph[a][idx]
                    break
            for idx, info in enumerate(graph[b]) :
                if info[0] == a :
                    info_b = info[:]
                    del graph[b][idx]
                    break
            # 경로가 제거되었을 경우의 최단 시간 업데이트
            t, _ = dajikstra(1)
            update_max_time = max(update_max_time, t)
            # 경로 추가
            graph[a].append(info_a)
            graph[b].append(info_b)
    # 6. 결과 출력
    print(-1 if update_max_time == float('inf') else update_max_time - min_time)
    
if __name__ == "__main__" :
    n, m = map(int, input().split())
    solution(n, m)