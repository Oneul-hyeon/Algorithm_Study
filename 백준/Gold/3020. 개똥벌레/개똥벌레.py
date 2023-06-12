import sys
input = sys.stdin.readline

n, h = map(int, input().split())
# 1. dp 생성
dp = [0] * (h+1)
# 2. 변화량 리스트 생성
change = [0] * (h+1)
# 3. 변화량 체크
for i in range(1, n+1) :
    obstacle = int(input())
    if i % 2 != 0 :
        up, bottom = obstacle, 1
    else :
        up, bottom = h, h-obstacle+1
    change[bottom-1] += 1
    change[up] -= 1

# 4. 변화량을 통해 파괴해야 하는 장애물 수 구하기
dp[0] = change[0]
for i in range(1, h+1) :
    dp[i] = dp[i-1] + change[i]
# 5. 결과 출력
print(f'{min(dp[:-1])} {dp[:-1].count(min(dp[:-1]))}')