import sys
input = sys.stdin.readline

# 1. dp 생성
dp = [0] * 251
# 2. 초기값 설정
dp[0], dp[1], dp[2] = 1, 1, 3
# 3.
for i in range(3, 251) :
    # 3-1. 점화식에 따라 처리
    dp[i] = dp[i-1] + 2 * dp[i-2]

# 4. 결과 출력
while True :
    try : print(dp[int(input())])
    except : break