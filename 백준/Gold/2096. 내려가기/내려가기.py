import sys
input = sys.stdin.readline

n = int(input())
idx_0, idx_1, idx_2 = map(int, input().split())

# 1. dp 생성
dp = [ [] for _ in range(2)]
# 2. 초기값 설정
dp[0] = [idx_0, idx_1, idx_2]
dp[1] = [idx_0, idx_1, idx_2]
# 3.
for _ in range(n-1) :
    # 3-1. 행 입력 받기
    idx_0, idx_1, idx_2 = map(int, input().split())
    # 3-2. 최대 점수 dp 처리
    # 3-2-1. 점화식에 따라 처리
    dp[0][0], dp[0][1], dp[0][2] = idx_0 + max(dp[0][0], dp[0][1]), idx_1 + max(dp[0][0], dp[0][1], dp[0][2]), idx_2 + max(dp[0][1], dp[0][2])

    # 3-3. 최소 점수 dp 처리
    # 3-3-1. 점화식에 따라 처리
    dp[1][0], dp[1][1], dp[1][2] = idx_0 + min(dp[1][0], dp[1][1]), idx_1 + min(dp[1][0], dp[1][1], dp[1][2]), idx_2 + min(dp[1][1], dp[1][2])
# 4. 결과 출력
print(f"{max(dp[0])} {min(dp[1])}")