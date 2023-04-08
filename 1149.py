import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline
n = int(input())
# 1. array에 집을 칠하는 비용 입력받기
array = [[0,0,0]] + [list(map(int, input().split())) for _ in range(n)]
# 2. dp 생성
dp = [ [0,0,0] for _ in range(n+1)]
# 3. dp[1] 값 설정
dp[1] = array[1]
# 4. 점화식에 따라 dp 채우기
for i in range(2, n+1) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + array[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + array[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + array[i][2]
# 5. dp[n]에서 가장 작은 값 출력
print(min(dp[-1]))