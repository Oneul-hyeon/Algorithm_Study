import sys
input = sys.stdin.readline

a, b, c, k = map(int, input().split())
# 1. 냅색 리스트 생성
dp = [[1000001] * (k+1) for _ in range(4)]
# 2. 초기값 설정
dp[0][0] = 0

# 3.
for j in range(k+1) :
    for cost, dir in [(a,1), (b, 3), (c, 2)] :
        # 3-1. 예외처리
        if j + cost > k : continue
        for i in range(4) :
            if dp[i][j] == 1000001 : continue
            # 3-2.
            direction = (i+dir) % 4
            dp[direction][j+cost] = min(dp[i][j] + 1, dp[direction][j+cost])

print(-1) if dp[0][k] == 1000001 else print(dp[0][k])