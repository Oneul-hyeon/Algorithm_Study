import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n) :
    for j in range(n) :
        if i == n-1 and j == n-1 : break
        # 1. 오른쪽으로 이동이 가능한 경우
        if j + graph[i][j] < n :
            dp[i][j + graph[i][j]] += dp[i][j]
        # 2. 아래쪽으로 이동이 가능한 경우
        if i + graph[i][j] < n :
            dp[i + graph[i][j]][j] += dp[i][j]

print(dp[-1][-1])