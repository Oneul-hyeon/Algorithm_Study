import sys, math
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs() :
    global count
    # 1-1. 점별 소요 시간 리스트 생성
    # 1-2. 큐에 (0, N) 삽입 <- (소요 시간, 점)
    queue = deque()
    queue.append((0, n))
    array[n] = 0
    # 1-3.
    while queue :
        # 큐에서 소요시간, 점 반환
        time, X = queue.popleft()
        for t, x in [[1, X-1], [1, X+1], [1, 2 * X]] :
            # 다음 소요 시간과, 지점 설정
            next_time = time + t
            # 점별 소요시간 리스트와 비교 후 업데이트
            if 0 <= x < 100001 and next_time <= array[x] :
                if x == k :
                    if next_time == count[0] : count[1] += 1
                    else : count = [next_time, 1]
                array[x] = next_time
                queue.append((next_time, x))

INF = math.inf
n, k = map(int, input().split())
array = [INF] * 100001
count = [0, 1]
bfs()
print(array[k])
print(count[1])