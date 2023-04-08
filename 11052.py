import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
array = [0] + array
# 1. dp 생성
dp = [0 for _ in range(n+1)]
# 2. dp[1] 값 설정
dp[1] = array[1]
# 3. dp[i] 값 설정
for i in range(2, n+1) :
    dp[i] = max([array[i]] + [dp[i-k] + dp[k] for k in range(1, i//2+1)])
# 4. dp[n] 값 출력
print(dp[n])