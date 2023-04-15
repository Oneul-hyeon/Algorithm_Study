import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. 체스판 생성
graph = [ [ 0 for _ in range(m+1)] for _ in range(n+1) ]

# 2. 퀸, 나이트, 폰 위치 입력 받기
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
now_queen = []
now_knight = []
# 3. 퀸, 나이트가 갈 수 있는 방향 선언
queen_dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (-1, 1), (1, -1), (1, 1)]
knight_dir = [(-2, -1), (-1, -2), (-1, 2), (-2, 1), (2, -1), (1, -2), (2, 1), (1, 2)]

# 4. dfs 함수 만들기 - 퀸 전용 dfs
def queen_dfs(x, y, dir) :
    nx, ny = x+dir[0], y+dir[1]
    # 4-1. graph 범위에서 벗어날 경우
    if nx < 1 or nx > n or ny <1 or ny > m : return
    # 4-2. 장애물 만났을 때
    if graph[nx][ny] == 2 : return
    graph[nx][ny] = 1
    queen_dfs(nx, ny, dir)

# 5. 체스판에 퀸, 나이, 폰 위치 설정 - 퀸, 나이트가 서 있는 위치도 장애물로 취급
# pawn 위치 먼저 설정
for i in range(1, len(pawn), 2) :
    graph[pawn[i]][pawn[i+1]] = 2
# queen 위치 먼저 설정
for i in range(1, len(queen), 2) :
    now_queen.append((queen[i], queen[i+1]))
    graph[queen[i]][queen[i+1]] = 2
# knight 위치 먼저 설정
for i in range(1, len(knight), 2) :
    now_knight.append((knight[i], knight[i+1]))
    graph[knight[i]][knight[i+1]] = 2

# 6. 퀸 먼저 이동하면서 이동 가능한 위치 찾기
for q in now_queen :
    for dir in queen_dir :
        x, y = q[0], q[1]
        queen_dfs(x, y, dir)
# 7. 나이트 이동하면서 이동 가능한 위치 찾기
for k in now_knight :
    x, y = k[0], k[1]
    for dir in knight_dir:
        nx, ny = x + dir[0], y + dir[1]
        if nx < 1 or nx > n or ny < 1 or ny > m: continue
        if graph[nx][ny] == 2: continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1

# 8. 나이트, 퀸, 폰이 존재하지 않는 위치 찾기
count = 0
for i in range(1, n+1) :
    for j in range(1, m+1) :
        if graph[i][j] == 0 :
            count += 1
print(count)