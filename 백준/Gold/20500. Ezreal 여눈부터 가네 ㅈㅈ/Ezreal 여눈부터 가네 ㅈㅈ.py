import sys
input = sys.stdin.readline

n = int(input())
# 1. dp 생성
dp = [0 for _ in range(1516)]
# 2. 초기값 설정
dp[2], dp[3] = 1, 1
# 3.
for i in range(4, n+1) :
    dp[i] = (2 * dp[i-2] + dp[i-1]) % 1_000_000_007
# 4. 결과 출력
print(dp[n])