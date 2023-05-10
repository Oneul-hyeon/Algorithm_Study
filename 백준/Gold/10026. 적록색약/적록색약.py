import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, state) :
    color = graph[x][y]
    queue = deque([])
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx<0 or nx>=n or ny<0 or ny>=n : continue
            # 적록색맹의 경우
            if state :
                if not Red_Green_Blindness_visited[nx][ny] :
                    # 색 비교
                    if (color == 'B' and graph[nx][ny] == 'B') or (color in ['R', 'G'] and graph[nx][ny] in ['R', 'G']) :
                        Red_Green_Blindness_visited[nx][ny] = True
                        queue.append((nx, ny))
            # 적록색맹이 아닐 경우
            else :
                if not visited[nx][ny] :
                    if color == graph[nx][ny] :
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    return True

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
# 1. 상하좌우 변수 선언
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 2. 방문여부 변수 선언
Red_Green_Blindness_visited = [[False for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
Red_Green_Blindness_count, count = 0, 0

# 3. 이중 for문
for i in range(n) :
    for j in range(n) :
        if not Red_Green_Blindness_visited[i][j] :
            if bfs(i, j, True) :
                Red_Green_Blindness_count += 1
        if not visited[i][j] :
            if bfs(i, j, False) :
                count += 1
print(count, Red_Green_Blindness_count)