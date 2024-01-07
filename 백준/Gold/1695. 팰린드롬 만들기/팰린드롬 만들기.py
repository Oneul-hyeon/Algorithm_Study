import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
# 1. DP 생성
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# 2.
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        # 2-1. 두 수가 같은 경우
        if array[-i] == array[j - 1] : dp[i][j] = dp[i-1][j-1] + 1
        # 2-2. 두 수가 다른 경우
        else : dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 4. 결과 출력
print(n - dp[-1][-1])