import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
# 1. 2차원 배열 생성하기
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# 2.
for i in range(1, n+1) :
    for j in range(1, k+1) :
        w = array[i][0]
        v = array[i][1]
        # 2-1. j(무게) < w 일 경우
        if j < w :
            dp[i][j] = dp[i-1][j]
        # 2-2. 그 외의 경우
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
# 3. 결과 출력
print(dp[n][k])