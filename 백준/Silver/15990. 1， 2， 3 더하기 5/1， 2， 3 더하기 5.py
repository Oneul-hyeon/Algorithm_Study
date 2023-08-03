import sys
input = sys.stdin.readline

t = int(input())
# 1. DP 생성
dp = [[0] * 3 for _ in range(100001)]
# 2. DP 초기값 설정
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
# 3.
for i in range(4, 100001) :
    # 3-1. 1을 추가하는 경우
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    # 3-2. 2를 추가하는 경우
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    # 3-3. 3을 추가하는 경우
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009
# 4. 결과 출력
for _ in range(t) :
    n = int(input())
    print(sum(dp[n]) % 1000000009)