import sys
input = sys.stdin.readline

# 1. dp 생성
dp = [0] * 1000001
# 2. 초기값 설정
dp[1], dp[2], dp[3] = 1, 2, 4
# 3.
for i in range(4, 1000001) :
    # 3-1. 점화식에 따라 처리
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009
# 4. 결과 출력
t = int(input())
for _ in range(t) :
    print(dp[int(input())])