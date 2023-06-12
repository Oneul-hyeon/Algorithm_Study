import sys
input = sys.stdin.readline

n, h = map(int, input().split())

dp = [0] * (h+1)
change = [0] * (h+1)

for i in range(1, n+1) :
    obstacle = int(input())
    if i % 2 != 0 :
        up, bottom = obstacle, 1
    else :
        up, bottom = h, h-obstacle+1
    change[bottom-1] += 1
    change[up] -= 1

dp[0] = change[0]
for i in range(1, h+1) :
    dp[i] = dp[i-1] + change[i]

print(f'{min(dp[:-1])} {dp[:-1].count(min(dp[:-1]))}')
