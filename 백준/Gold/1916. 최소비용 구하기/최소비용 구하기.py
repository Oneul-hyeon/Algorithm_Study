import sys, math, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

# 1. n+1의 리스트 만들기
array = [[] for _ in range(n+1)]
# 2. 거리 리스트 만들기
distance = [math.inf for _ in range(n+1)]
# 3. 간선 정보 입력받기
for _ in range(m) :
    a, b, c = map(int, input().split())
    array[a].append((b,c))

starting_point, destination = map(int, input().split())
# 4. 다익스트라 재귀함수 생성
def dijkstra(start) :
    # 5. 힙에 사용할 리스트 생성
    heap = []
    # 6. 힙에 (0, 시작지점) push
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    # 7.
    while heap :
        # 8. 힙에서 (거리, 노드) 추출
        dist, now = heapq.heappop(heap)
        # 9. 이미 처리된 노드라면 무시
        if dist > distance[now] : continue
        # 10. 인접 노드 확인
        for i in array[now] :
            # 11. 비용 계산
            cost = dist + i[1]
            # 12. 해당 노드를 거쳐 가는 게 더 짧을 경우
            if cost < distance[i[0]] :
                # 12-1. 거리 재설정
                distance[i[0]] = cost
                # 12-2. 힙에 (현재 거리 비용, 노드) push
                heapq.heappush(heap, (cost, i[0]))
# 13. 다익스트라 알고리즘 실행
dijkstra(starting_point)
# 14. 결과 출력
print(distance[destination])

