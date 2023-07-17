import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(x, y):
    # 1-1. 큐에 현재 위치 삽입
    queue = deque()
    queue.append((x, y))
    # 1-2. 현재 위치 방문 처리
    visited[x][y] = True
    idx = 1
    # 1-3.
    while queue :
        x, y = queue.popleft()
        for dir_x, dir_y in dirs :
            # 상하좌우 4방향
            nx, ny = x + dir_x, y + dir_y
            # 예외처리
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            # 다음 위치 값이 1이면서 방문하지 않은 경우
            if graph[nx][ny] == 1 and not visited[nx][ny] :
                idx += 1
                # 방문처리
                visited[nx][ny] = True
                # 위치 값 바꾸기
                graph[nx][ny] = idx
                # 큐에 다음 위치 생성
                queue.append((nx, ny))
    return idx


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * n for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        # 2-1. 해당 위치값이 1이면서 방문하지 않은 경우
        if graph[i][j] == 1 and not visited[i][j]:
            # bfs 실행
            answer.append(bfs(i, j))

# 3. 결과 출력
print(len(answer))
for i in sorted(answer) : print(i)