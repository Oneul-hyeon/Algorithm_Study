import sys
input = sys.stdin.readline

# 1. 현재 칸 청소 함수 정의
def cleaning(x, y) :
    global visited

    # 1-1. 현재 위치가 청소되지 않은 경우 청소
    if not visited[x][y] : visited[x][y] = True
# 2. 주변 칸 청소 여부 확인 함수 정의
def check(x, y) :
    # 2-1. 청소되지 않은 칸이 있는 경우 False 반환
    for dir_x, dir_y in dirs :
        nx, ny = x + dir_x, y + dir_y
        if not graph[nx][ny] and not visited[nx][ny] :
            return False
    # 2-2. 모두 청소되었다면 True 반환
    return True

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 3. 청소 여부 리스트 생성
visited = [[False for _ in range(m)] for _ in range(n)]
# 4. 방향 리스트 생성
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 5.
while True :
    # 5-1. 현재 위치 청소
    cleaning(r, c)
    # 5-2. 주변 칸이 모두 청소된 경우
    if check(r, c) :
        # 5-2-1. 후진이 가능한 경우
        back_d = (d + 2) % 4
        br, bc = r + dirs[back_d][0], c + dirs[back_d][1]
        if graph[br][bc] != 1 :
            # 현재 위치 변경
            r, c = br, bc
        # 5-2-2. 후진이 불가능한 경우
        else :
            # while문 탈출
            break
    # 5-3. 주변에 청소 안 된 칸이 있는 경우
    else :
        # 5-3-1. 반시계 방향으로 회전
        d = (d - 1) % 4
        # 5-3-2. 앞 칸이 청소되지 않은 경우 전진
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        if not graph[nr][nc] and not visited[nr][nc] :
            r, c = nr, nc
# 6. 결과 출력
ans = 0
for row in visited :
    ans += row.count(True)
print(ans)