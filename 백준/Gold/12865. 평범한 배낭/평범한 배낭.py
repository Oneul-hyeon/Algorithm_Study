import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 1. 배낭에 넣을 수 있는 물건들 입력받기
bag = [list(map(int, input().split())) for _ in range(n)]
# 2. 1차원 dp 생성
dp = [0] * (k+1)
# 3.
for i in range(n) :
    for j in range(k, -1, -1) :
        w = bag[i][0]
        v = bag[i][1]
        if j >= w :
            # 4. 점화식에 따라 dp 처리
            dp[j] = max(dp[j], dp[j-w] + v)
# 5. 결과 출력
print(dp[-1])