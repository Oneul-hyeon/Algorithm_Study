import sys
input = sys.stdin.readline

n = int(input())
board = [0] + list(map(int, input().split()))
# 1. dp 생성
dp = [[0] * (n+1) for _ in range(n+1)]
# 2. 자기 자신에 대해 팰린드롬 처리
# 3. 두 번째 글자까지 팰린드롬 처리
for i in range(1, n+1) :
    dp[i][i] = 1
    if i < n :
        if board[i] == board[i+1] : dp[i][i+1] = 1
# 4. 점화식에 따라 팰린드롬 처리
for cnt in range(2, n+1) :
    for i in range(1, n-1) :
        if i + cnt <= n :
            j = i + cnt
            if board[i] == board[j] and dp[i+1][j-1] :
                dp[i][j] = 1
# 5. 결과 출력
m = int(input())
for _ in range(m) :
    s, e = map(int, input().split())
    print(dp[s][e])