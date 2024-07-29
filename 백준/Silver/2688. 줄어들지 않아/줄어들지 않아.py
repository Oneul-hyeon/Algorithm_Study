import sys
input = sys.stdin.readline

# 1. 2차원 dp 생성
dp = [ [0 for _ in range(10)] for _ in range(65)]
# 2. 초기값 설정
dp[1] = [1 for _ in range(10)]
# 3.
for i in range(2, 65) :
    for j in range(10) :
        # 3-1. 점화식에 따라 처리
        dp[i][j] = sum(dp[i-1][:j+1])
# 4. 결과 리스트 생성
result = [sum(row) for row in dp]
# 5.
for _ in range(int(input())) :
    # 5-1. 결과 출력
    print(result[int(input())])