import sys, math, heapq
input = sys.stdin.readline

INF = math.inf

n, d = map(int, input().split())
# 1. (d+1) 길이의 dp 생성 <- 값은 무한으로
dp = [INF] * (d+1)
dp[0] = 0
# 2. 힙리스트 생성
heap = []
# 3. 힙 리스트에 지름길 정보 push
for _ in range(n):
    heapq.heappush(heap, list(map(int, input().split())))
for i in range(d+1) :
    if i != 0 :
        # 4-1. 점화식대로 값 설정
        dp[i] = min(dp[i], dp[i-1] + 1)
    # 4-2. while문을 이용해 지름길 처리
    if heap :
        while heap[0][0] == i :
            start, end, dist = heapq.heappop(heap)
            if end <= d : 
                dp[end] = min(dp[end], dp[start]+dist)
            if not heap : break
# 5. 결과 출력
print(dp[d])