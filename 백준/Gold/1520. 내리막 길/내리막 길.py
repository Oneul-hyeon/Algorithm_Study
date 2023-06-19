import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 4. 재귀함수 선언
def dfs(x, y) :
    # 5. 종료 조건 1 : 목표 인덱스에 도착했을 경우
    if (x, y) == (n-1, m-1) :
        return 1
    # 6. 종료 조건 2 : 방문한 적 있는 경우
    if dp[x][y] != -1 : return dp[x][y]
    # 7. 방문한 적이 없는 경우 방문 처리(-1이 아닐 경우 방문)
    dp[x][y] = 0
    # 8. 4방향으로 탐색
    for dir_x, dir_y in dirs :
        nx, ny = x + dir_x, y + dir_y
        # 9. 예외 처리
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        # 10. 조건에 따라 진행
        if graph[nx][ny] < graph[x][y] :
            dp[x][y] += dfs(nx, ny)
    # 11. 종료 조건 3 : 해당 인덱스로부터 탐색 종료 시
    return dp[x][y]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 1. dp 생성
dp = [[-1] * m for _ in range(n)]
# 2. dfs 실행
# 3. 결과 출력
print(dfs(0, 0))