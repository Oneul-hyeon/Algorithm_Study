import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 3차원 dp 생성
dp = [ [ [0, 0, 0] for _ in range(n)] for _ in range(n)]
# 2. 초기값 설정
dp[0][1][0] = 1
# 3.
for i in range(n) :
    for j in range(n) :
        if (i, j) in [(0, 0), (0, 1)] : continue
        # 3-1. 현재 위치에 벽이 없을 경우
        if not graph[i][j] :
            # 3-1-1. 가로 형태 처리
            # 이전 위치가 가로 형태가 가능할 경우 처리
            if j - 1 >= 0 : dp[i][j][0] += dp[i][j-1][0]
            # 이전 위치가 대각선 형태가 가능할 경우 처리
            if i - 1 >= 0 and j - 1 >= 0 : dp[i][j][0] += dp[i][j-1][2]

            # 3-1-2. 세로 형태 처리
            # 이전 위치가 세로 형태가 가능할 경우 처리
            if i - 1 >= 0 : dp[i][j][1] += dp[i-1][j][1]
            # 이전 위치가 대각선 형태가 가능할 경우 처리
            if i - 1 >= 0 and j - 1 >= 0 : dp[i][j][1] += dp[i-1][j][2]
        # 3-2. 현재 위치, 왼쪽, 위쪽이 맵 안에 포함되면서 벽이 아닐 경우
        if i - 1 >= 0 and j - 1 >= 0 and not graph[i][j] and not graph[i][j-1] and not graph[i-1][j] :
            # 이전 위치가 가로 형태 처리
            # 이전 위차가 세로 형태 처리
            # 이전 위치가 대각선 형태 처리
            dp[i][j][2] += sum(dp[i-1][j-1])
# 4. 결과 출력
print(sum(dp[-1][-1]))