import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
# 1. 2차원 배열 생성하기
dp = [0 for _ in range(k+1)]

# 2.
for i in range(n+1) :
    for j in range(k, -1, -1) :
        w = array[i][0]
        v = array[i][1]
        if j >= w :
            dp[j] = max(dp[j], dp[j-w] + v)
# 3. 결과 출력
print(dp[k])
