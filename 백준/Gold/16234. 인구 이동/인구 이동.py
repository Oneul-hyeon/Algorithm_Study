import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, visited) :
    visited[x][y] = True
    index_lst = [(x, y)]
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()
        for dir_x, dir_y in dirs :
            nx, ny = x + dir_x, y + dir_y
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if not visited[nx][ny] :
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r :
                    visited[nx][ny] = True
                    index_lst.append((nx, ny))
                    queue.append((nx, ny))
    if len(index_lst) == 1 : return True
    else :
        summation = int(sum([graph[x][y] for x, y in index_lst]) / len(index_lst))
        for x, y in index_lst :
            graph[x][y] = summation
        return False

def check() :
    global ans
    visited = [[False] * n for _ in range(n)]
    state = True
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                if not bfs(i, j, visited) :
                    if state : state = False
    if not state : ans += 1
    return state
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
while True :
    if check() : break
print(ans)