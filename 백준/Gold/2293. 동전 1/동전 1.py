import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# 1. DP 생성
dp = [0 for _ in range(k+1)]
# 2. 초기값 설정
dp[0] = 1
# 3. 동전 정렬
coins.sort()
# 4.
for coin in coins :
    # 4-1.
    for i in range(coin, k+1) :
        # 점화식에 따라 처리
        dp[i] += dp[i-coin]
# 5. 결과 출력
print(dp[k])