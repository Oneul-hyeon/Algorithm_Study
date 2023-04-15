import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
array = [0] + [int(input()) for _ in range(n)]
# 1. dp 생성
dp = [0 for _ in range(301)]

if n == 1 :
    print(array[1])
elif n == 2 :
    print(array[1]+array[2])
else:
    # 2. dp[1] ~ dp[3]까지 값 설정
    dp[1], dp[2] = array[1], array[1]+array[2]
    dp[3] = max(array[1]+array[3], array[2]+array[3])
    # 3. dp 값 채우기
    for i in range(4, n+1) :
        dp[i] = max(dp[i-3]+array[i-1]+array[i], dp[i-2]+array[i])
    # 4. 결과 출력
    print(dp[n])