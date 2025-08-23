import sys
input = sys.stdin.readline

T, W = map(int, input().split())

# 1. dp 생성
dp = [[0 for _ in range(W+1)] for _ in range(T+1)]
# 2.
for t in range(1, T+1):
    # 2-1. 초기값 설정
    dp[t][0] = dp[t-1][0] + int((tree:=int(input()))==1)
    # 2-2.
    for w in range(1, W+1 if t>=W else t+1):
        # 2-2-1. 자두를 먹을 수 있는 경우
        if (now:=w%2+1) == tree:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1]) + 1
        # 2-2-2. 자두를 먹을 수 없는 경우
        else :
            dp[t][w] = dp[t-1][w]
# 3. 결과 출력
print(max(dp[-1]))