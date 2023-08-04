import sys
input = sys.stdin.readline

def count_path(x, y) :
    dp = [[1] * y for _ in range(x)]
    for i in range(1, x) :
        for j in range(1, y) :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

n, m, k = map(int, input().split())
if k == 0 :
    print(count_path(n, m))
else :
    # 1. k 번의 인덱스 구하기
    if k % m != 0 :
        k_x, k_y = k // m , k % m
    else :
        k_x, k_y = k // m - 1 , m

    # 2. 시작점부터 중간 지점까지의 행렬 구하기
    x1, y1 = k_x+1, k_y
    # 3. 중간 지점부터 목적지까지의 행렬 구하기
    x2, y2 = n - x1 + 1, m - y1 + 1
    print(count_path(x1, y1) * count_path(x2, y2))