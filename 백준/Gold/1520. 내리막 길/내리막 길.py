import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y) :
    # 종료 조건 : 목표 인덱스에 도착했을 경우
    if (x, y) == (n-1, m-1) :
        return 1
    # 종료 조건 : 방문한 적 있는 경우
    if dp[x][y] != -1 : return dp[x][y]
    dp[x][y] = 0
    for dir_x, dir_y in dirs :
        nx, ny = x + dir_x, y + dir_y
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        if graph[nx][ny] < graph[x][y] :
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * m for _ in range(n)]
print(dfs(0, 0))