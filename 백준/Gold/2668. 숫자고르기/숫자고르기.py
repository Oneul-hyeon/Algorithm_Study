import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(node) :
    global ans

    # 1-1. 경로 변수 생성
    route = set([node])
    # 1-2. 큐 생성 후 현재 위치 삽입
    queue = deque([node])
    # 1-3.
    while queue :
        # 1-3-1. 위치 인덱스 반환
        now = queue.popleft()
        # 1-3-2. 도착지 생성
        next = array[now]
        # 1-3-3. 이미 온 적이 있는 경우
        if next in route :
            # 해당 위치가 출발지일 경우(사이클이 형성되는 경우)
            if next == node :
                # 정답 집합 업데이트
                ans = ans | route
            return
        # 1-3-4. 온 적이 없는 경우
        # 큐에 현재 위치 삽입
        queue.append(next)
        # 경로 변수 업데이트
        route.add(next)

n = int(input())
array = [0] + [int(input()) for _ in range(n)]

# 2. 정답 집합 생성
ans = set()
# 3.
for i in range(1, n+1) :
    # bfs 실행
    bfs(i)
# 4. 결과 출력
print(len(ans))
for node in sorted(ans) : print(node)