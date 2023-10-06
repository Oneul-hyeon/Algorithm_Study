import sys
from collections import defaultdict
input = sys.stdin.readline

ans = 0
def solution(n, m, empty) :
    # 1. 그래프 생성
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # 2. 초기값 설정
    dp[1][1] = 1
    # 3. 구멍 위치 딕셔너리 생성
    empty_dict = defaultdict(int)
    for x, y in empty :
        empty_dict[(x, y)] = True
    # 4.
    for y in range(1, m+1) :
        for x in range(1, n+1) :
            if empty_dict[(x, y)] : continue
            # 방향 인덱스 생성
            dirs = [(-1, 1), (0, 1), (1, 0)] if y % 2 != 0 else [(0, 1), (1, 1), (1, 0)]
            for dir_x, dir_y in dirs :
                nx, ny = x + dir_x, y + dir_y
                # 예외 처리
                if nx < 1 or nx > n or ny < 1 or ny > m or empty_dict[(nx, ny)] : continue
                dp[nx][ny] += dp[x][y]
    # 5. 결과 출력
    print(dp[n][m] % (10**9 + 7))

if __name__ == "__main__" :
    n, m = map(int, input().split())
    k = int(input())
    empty = [list(map(int, input().split())) for _ in range(k)]
    solution(n, m, empty)