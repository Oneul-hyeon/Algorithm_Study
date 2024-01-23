import sys
input = sys.stdin.readline

t = int(input())
# 1. dp 생성
dp = [[[0, 0] for _ in range(101)] for _ in range(101)]
# 2. 초기값 설정
dp[1][0] = [1, 1]
# 3.
for n in range(2, 101) :
    for k in range(n) :
        # 점화식에 따라 처리
        dp[n][k][0] = dp[n-1][k][0] + dp[n-1][k][1]
        dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]
# 4. 결과 출력
for _ in range(t) :
    n, k = map(int, input().split())
    print(sum(dp[n][k]))