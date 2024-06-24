import sys
input = sys.stdin.readline

n = int(input())

# 1. dp 생성
dp = [0 for _ in range(n + 1)]
# 2. 현재 최댓값 변수 생성
max_profit = 0
# 3.
for i in range(n) :
    t, p = map(int, input().split())
    # 3-1. 현재 최댓값 업데이트
    max_profit = max(max_profit, dp[i])
    # 3-2. 범위를 벗어나는 경우 continue
    if i + t > n : continue
    # 3-3. 점화식에 따라 처리
    dp[i + t] = max(dp[i + t], max_profit + p)
# 4. 최댓값 출력
print(max(dp))