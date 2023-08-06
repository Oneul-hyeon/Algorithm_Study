import sys
input = sys.stdin.readline

a, b, c, k = map(int, input().split())
# 1. 2차원 dp 생성
dp = [[1000001] * (k+1) for _ in range(4)]
# 2. 초기값 설정
dp[0][0] = 0

# 3.
for j in range(k+1) :
    for cost, dir in [(a,1), (b, 3), (c, 2)] :
        # 3-1. 예외처리
        if j + cost > k : continue
        # 3-2.
        for i in range(4) :
            # 예외 처리
            if dp[i][j] == 1000001 : continue
            # 점화식에 따라 처리
            direction = (i+dir) % 4
            dp[direction][j+cost] = min(dp[i][j] + 1, dp[direction][j+cost])
# 4. 결과 출력
print(-1) if dp[0][k] == 1000001 else print(dp[0][k])