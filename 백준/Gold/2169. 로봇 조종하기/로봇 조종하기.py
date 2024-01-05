import sys
input = sys.stdin.readline

def solution(n, m, array):
    # 1. DP 생성
    dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
    # 2. 초기값 설정
    dp[0][0] = [array[0][0]] * 2
    for y in range(1, m) : dp[0][y] = [dp[0][y-1][0] + array[0][y]] * 2
    # 3.
    for x in range(1, n) :
        for y in range(m) :
            # 3-1. 점화식에 따라 이전 행 정보 가져오기
            dp[x][y] = [max(dp[x-1][y]) + array[x][y]] * 2
        for y in range(m) :
            L2R, R2L = y, m - 1 - y
            # 3-2 왼쪽에서 오른쪽으로 이동이 가능한 경우 점화식에 따라 처리
            if L2R + 1 < m : dp[x][L2R+1][0] = max(dp[x][L2R+1][0], dp[x][L2R][0] + array[x][L2R+1])
            # 3-3. 오른쪽에서 왼쪽으로 이동이 가능한 경우
            if R2L - 1 >= 0 : dp[x][R2L-1][1] = max(dp[x][R2L-1][1], dp[x][R2L][1] + array[x][R2L-1])
    # 4. 결과 출력
    print(max(dp[-1][-1]))

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, array)