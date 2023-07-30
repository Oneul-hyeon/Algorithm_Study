import sys, math
input = sys.stdin.readline

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
INF = math.inf
# dp 생성
dp = [INF] * (c+101)
dp[0] = 0
for cost, customer in city :
    for i in range(1, len(dp)) :
        if i >= customer :
            dp[i] = min(dp[i], dp[i - customer] + cost)
print(min(dp[c:]))