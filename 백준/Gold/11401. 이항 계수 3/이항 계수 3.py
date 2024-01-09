import sys
input = sys.stdin.readline

# 1. 제곱 함수 정의
def pow(x, p) :
    # 1-1. 종료 조건 설정
    if p == 1 : return x
    # 1-2. p // 2 값 구하기
    value = pow(x, p // 2) % mod
    # 1-3. 제곱값 리턴
    if p % 2 == 0 : return value * value
    else : return value * value * x

n, k = map(int, input().split())
mod = 1_000_000_007
# 2. dp 생성
dp =[0 for _ in range(n+1)]
# 3. 초기값 설정
dp[0], dp[1] = 1, 1
# 4.
for i in range(2, n+1) : dp[i] = i * dp[i-1] % mod
# 5.결과 출력
print(dp[n] * pow(dp[n-k] * dp[k], mod - 2) % mod)