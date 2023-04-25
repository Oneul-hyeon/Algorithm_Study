import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 1. 변수 입력받기
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    # 2. dp 생성
    dp = [0] * (m+1)
    # 3. dp[0] 값 설정
    dp[0] = 1
    for coin in coins :
        for i in range(coin, m+1) :
            # 5. 점화식 처리
            dp[i] += dp[i-coin]
    print(dp[m])