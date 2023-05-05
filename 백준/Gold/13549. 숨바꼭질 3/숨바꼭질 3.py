import sys, math, heapq
input = sys.stdin.readline

INF = math.inf
# 1. n, k 입력받기
n, k = map(int, input().split())
# 2. 위치 리스트 만들기
array = [INF] * 100001
# 3. 다익스트라 재귀 함수 정의
def dijkstra(start) :
    # 4. 힙 리스트 선언
    heap = []
    array[start] = 0
    heapq.heappush(heap, (0, start))
    while heap :
        # 7. 힙에서 (시간, 노드) 정보 꺼내기
        time, node = heapq.heappop(heap)
        # 8. 이미 처리되었다면 continue
        if time > array[node] : continue
        for i in [[1, node-1], [1, node+1], [0, 2*node]] :
            # 10. 시간 계산
            next_time = time + i[0]
            # 11. 해당 노드를 거쳐가는 게 빠를 경우 힙에 (시간, 노드) push
            if 0 <= i[1] < 100001 and next_time < array[i[1]] :
                array[i[1]] = next_time
                heapq.heappush(heap, (next_time, i[1]))

# 12. 다익스트라 재귀 함수 실행
dijkstra(n)
# 13. 결과 출력
print(array[k])