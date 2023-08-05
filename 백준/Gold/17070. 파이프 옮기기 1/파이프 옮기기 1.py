import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 1. dp 생성
dp = [[[0] * n for _ in range(n)] for _ in range(n)]
# 2. 초기값 설정
for i in range(1, n) :
    if not graph[0][i] : dp[0][0][i] = 1
    else : break
# 3.
for i in range(1, n) :
    for j in range(1, n) :
        # 3-1. 가로, 세로의 경우
        if not graph[i][j] :
            # 점화식에 따라 처리
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        # 3-2. 대각일 경우
        if not graph[i][j] and not graph[i-1][j] and not graph[i][j-1] :
            # 점화식에 따라 처리
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
# 4. 결과 출력
print(sum([dp[i][-1][-1] for i in range(3)]))