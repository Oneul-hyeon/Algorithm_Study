import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# 1. 뱀의 몸 리스트 생성
snake = deque()
snake.append((1, 1))
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
k = int(input())
# 2. 사과 정보 입력
for _ in range(k) :
    x, y = map(int, input().split())
    graph[x][y] = 2
# 3. 방향 정보 리스트 생성
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 1 # 처음엔 오른쪽을 보고 있음
# 4.
l = int(input())
i, j = 1, 1
graph[1][1] = 1
ans = 0
info = [list(map(str, input().rstrip().split())) for _ in range(l)]
while True :

    # 4-1. 다음 인덱스 지정
    i, j = i + dirs[dir][0], j + dirs[dir][1]
    # 4-2. 다음 위치가 벽이거나 몸일 경우
    if i < 1 or i > n or j < 1 or j > n or graph[i][j] == 1 :
        print(ans + 1)
        exit()
    # 4-3. 다음 위치가 벽이거나 몸이 아닐 경우
    else :
        # 다음 위치를 뱀의 몸 리스트에 삽입
        snake.append((i, j))
        # 다음 위치가 빈 공간일 경우
        if graph[i][j] == 0 :
            p_i, p_j = snake.popleft()
            graph[p_i][p_j] = 0
        # 뱀의 머리 위치시키기
        graph[i][j] = 1
        # 카운팅
        ans += 1
    # 4-4. 방향 바꿔주기
    if info:
        if int(info[0][0]) == ans :
            c = info[0][1]
            if c == 'L' :
                dir = (dir - 1) % 4
            else :
                dir = (dir + 1) % 4
            info.pop(0)