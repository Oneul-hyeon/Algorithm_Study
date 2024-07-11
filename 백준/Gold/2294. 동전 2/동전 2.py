import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set()
for _ in range(n) :
    coin = int(input())
    if coin <= k :
        coins.add(coin)

# 1. dp 생성
dp = [100_001 for _ in range(k+1)]
# 2. 초기값 설정
dp[0] = 0
# 3.
for c in list(coins) :
    for i in range(c, k+1) :
        dp[i] = min(dp[i], dp[i-c] + 1)
# 4. 결과 출력
print(dp[-1] if dp[-1] != 100_001  else -1)