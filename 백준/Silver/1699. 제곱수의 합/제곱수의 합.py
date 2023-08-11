import sys
input = sys.stdin.readline

n = int(input())
# 1. dp 생성
dp = [sys.maxsize] * (n+1)
# 2. 초기값 설정
dp[0], dp[1] = 0, 1
# 3.
for i in range(2, n+1) :
    # 3-1. 제곱근이 정수일 경우
    if int(i**.5) == i**.5 : dp[i] = 1
    # 3-2. 이외의 경우
    else :
        for j in range(1, int(i**.5)+1) :
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
# 3. 결과 출력
print(dp[n])