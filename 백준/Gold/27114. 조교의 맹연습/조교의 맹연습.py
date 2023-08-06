import sys
input = sys.stdin.readline

a, b, c, k = map(int, input().split())
# 1. 냅색 리스트 생성
dp = [[sys.maxsize] * (4) for _ in range(k+1)]
# 2. 초기값 설정
dp[0][0] = 0

# 3.
for i in range(k+1) :
    for cost, dir in [(a,1), (b, 3), (c, 2)] :
        # 3-1. 예외처리
        if i + cost > k : continue
        for j in range(4) :
            # 3-2.
            dp[i+cost][(j+dir)%4] = min(dp[i][j] + 1, dp[i+cost][(j+dir)%4])

print(-1) if dp[k][0] == sys.maxsize else print(dp[k][0]) 