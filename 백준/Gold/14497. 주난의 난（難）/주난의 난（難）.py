import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
graph = [list(map(str, input().rstrip())) for _ in range(n)]
graph[x1][y1], graph[x2][y2] = '0', '1'
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * m for _ in range(n)]

queue = deque()
queue.append((x1, y1))
visited[x1][y1] = True
while queue :
    x, y = queue.popleft()
    for dir_x, dir_y in dirs :
        nx, ny = x + dir_x, y + dir_y
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        if not visited[nx][ny] :
            visited[nx][ny] = True
            if graph[nx][ny] == '0' :
                queue.appendleft((nx, ny))
                graph[nx][ny] = int(graph[x][y])
            else :
                queue.append((nx, ny))
                graph[nx][ny] = int(graph[x][y]) + 1

print(graph[x2][y2])