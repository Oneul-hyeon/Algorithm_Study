import sys
input = sys.stdin.readline

n = int(input())
# 1. dp 생성
dp = [0] * (n+1)
if n > 1 :
    # 2. dp 초기값 설정
    dp[2] = 2
    # 3.
    for i in range(3, n+1) :
        # 3-1. 점화식에 따라 처리
        dp[i] = (dp[i-1] * 3) % 1000000009
# 4. 결과 출력
print(dp[n])