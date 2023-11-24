import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 1. 다익스트라 함수 정의
def djikstra(start, n) :
    node = [[] for _ in range(n+1)]
    # 1-1. 간선 정보 입력
    for _ in range(m) :
        a, b, c = map(int, input().split())
        node[a].append((b, c))
        node[b].append((a, c))
    # 1-2. 거리 정보 리스트 생성
    INF = float('INF')
    distance = [INF for _ in range(n+1)]
    # 1-3. 힙 리스트 생성 후 (시작 노드, 거리) 정보 입력
    heap = []
    heappush(heap, (start, 0))
    # 1-4. 거리 정보 리스트에 진서네 집 거리 설정
    distance[start] = 0
    # 1-5.
    while heap :
        # 1-5-1. 노드, 거리 정보 반환
        now, d = heappop(heap)
        # 1-5-2. 이미 처리된 경우 continue
        if distance[now] < d : continue
        # 1-5-3.
        for nn, c in node[now] :
            # 거리 계산
            cost = d + c
            # 계산된 거리가 현재 거리 리스트의 거리보다 짧을 경우
            if distance[nn] > cost :
                # 거리 정보 업데이트
                distance[nn] = cost
                # 힙에 (다음 노드, 거리) 정보 입력
                heappush(heap, (nn, cost))
    # 1-6. 거리 정보 리스트 반환
    return distance
def solution(n, m, j, k, home_A, home_B) :
    # 2. 다익스트라 함수 실행
    distance = djikstra(j, n)
    # 3. A형, B형 모두 진서네 집에 갈 수 없는 경우
    INF = float('INF')
    home_A_dist = [distance[idx] for idx in home_A]
    home_B_dist = [distance[idx] for idx in home_B]
    if home_A_dist.count(INF) + home_B_dist.count(INF) == 2 * k : print(-1)
    # 4. 이외의 경우
    else :
        # A와 B의 최소 거리가 같을 경우
        # A의 최소 거리가 더 가까울 경우
        if min(home_A_dist) <= min(home_B_dist) : print(f'A\n{min(home_A_dist)}')
        # B의 최소 거리가 더 가까울 경우
        else : print(f'B\n{min(home_B_dist)}')

if __name__ == "__main__" :
    n, m = map(int, input().split())
    j, k = int(input()), int(input())
    home_A, home_B = list(map(int, input().split())), list(map(int, input().split()))
    solution(n, m, j, k, home_A, home_B)