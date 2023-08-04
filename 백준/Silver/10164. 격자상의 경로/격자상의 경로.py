import sys
input = sys.stdin.readline
# 1. 경로 수 반환 함수 정의
def count_path(x, y) :
    # 1-1. dp 생성
    dp = [[1] * y for _ in range(x)]
    # 1-2. 점화식에 따라 처리
    for i in range(1, x) :
        for j in range(1, y) :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 1-3. 경로 수 반환
    return dp[-1][-1]

n, m, k = map(int, input().split())
# 2. k=0인 경우 시작점에서 도착점으로 가는 경로 출력
if k == 0 :
    print(count_path(n, m))
# 3. k=0이 아닌 경우
else :
    # 3-1. k가 위치하는 인덱스 구하기
    if k % m != 0 :
        k_x, k_y = k // m , k % m
    else :
        k_x, k_y = k // m - 1 , m
    # 3-2. 시작점부터 k까지의 행렬 크기 구하기
    x1, y1 = k_x+1, k_y
    # 3-3. k부터 도착점까지의 행렬 크기 구하기
    x2, y2 = n - x1 + 1, m - y1 + 1
    # 3-4. 총 경로 출력
    print(count_path(x1, y1) * count_path(x2, y2))