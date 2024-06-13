import sys
input = sys.stdin.readline

n, t = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 1. dp 생성
dp = [0 for _ in range(t+1)]
# 2.
for k, s in array :
    # 2-1.
    for i in range(t, k-1, -1) :
        # 2-1-1. dp 값 업데이트
        dp[i] = max(dp[i], dp[i-k] + s)
# 3. 결과 출력
print(dp[-1])