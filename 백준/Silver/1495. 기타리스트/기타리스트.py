import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
array = list(map(int, input().split()))

# 1. 2차원 dp 생성
dp = [[False] * (m+1) for _ in range(n+1)]
# 2. 시작 볼륨 처리
dp[0][s] = True

# 3.
for i in range(1, n+1) : # 곡의 개수 
    for j in range(m+1) : # 최대 볼륨
        # 4. 직전 곡의 볼륨값으로 가능한 값을 가질 경우
        if dp[i-1][j] :
            # 4-1. 이번 곡의 볼륨값으로 가능한 값을 가질 경우 처리
            if 0 <= j+array[i-1] <= m :
                dp[i][j+array[i-1]] = True
            if 0 <= j-array[i-1] <= m :
                dp[i][j-array[i-1]] = True

# 5. 마지막 곡의 가능한 값 출력
for j in range(m, -1, -1) :
    if dp[-1][j] :
        print(j)
        break
else : print(-1)