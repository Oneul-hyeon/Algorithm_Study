import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
visited = [False] * (n+1)
# 1. 큐에 현재 위치 삽입
queue = deque()
queue.append((a, 0))
visited[a] = True
# 2.
while queue :
    # 2. 위치 인덱스 반환
    now, jump = queue.popleft()
    # 3. 종료 조건 탐색
    if (b - now) % array[now] == 0 : print(jump + 1); exit()
    d = array[now]
    # 4. 왼쪽으로 점프
    for next in range(now, 0 , - d) :
        if not visited[next] :
            visited[next] = True
            queue.append((next, jump + 1))
    # 5. 오른쪽으로 점프
    for next in range(now + d, n, d) :
        if not visited[next] :
            visited[next] = True
            queue.append((next, jump + 1))

# 6. 도달하지 못 하는 경우
print(-1)