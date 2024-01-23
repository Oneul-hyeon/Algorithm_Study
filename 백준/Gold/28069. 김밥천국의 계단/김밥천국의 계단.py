import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 1. dp 생성
dp = [float("INF") for _ in range(n+1)]
# 2. 초기값 설정
dp[0] = 0
# 3.
for i in range(1, n+1) :
    # 3-1. 이전 계단에서 올라오는 경우
    dp[i] = min(dp[i], dp[i-1] + 1)
    # 3-2. 순간이동이 가능한 경우
    if i + i // 2 <= n :
        dp[i + i // 2] = min(dp[i + i // 2], dp[i] + 1)
# 4. 결과 출력
print("minigimbob" if dp[-1] <= k else "water")