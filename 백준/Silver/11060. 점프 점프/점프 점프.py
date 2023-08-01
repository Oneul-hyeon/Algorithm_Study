import sys
input = sys.stdin.readline

n = int(input())
miro = list(map(int, input().split()))
dp = [n+1] * n
dp[0] = 0
for i in range(n) :
    for j in range(1, miro[i]+1) :
        if i + j >= n : break
        dp[i+j] = min(dp[i+j], dp[i] + 1)

print(dp[-1]) if dp[n-1] != n+1 else print(-1)