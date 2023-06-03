import sys
input = sys.stdin.readline

def check(x, y) :
    for i in range(4) :
        nx, ny = x + dirs[i][0], y + dirs[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        if not graph[nx][ny] : return False
    return True

n, m = map(int, input().split())
# 1. 현재 위치와 방향 입력 받기
i, j, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 2. 방향 리스트 생성
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
# 3
while True :
    # 4. 현재 칸이 청소되지 않은 경우 청소
    if not graph[i][j] : graph[i][j] = 2; ans += 1
    # 5. 현재 위치 기준 4방향 체크
    # 6. 청소되지 않은 칸이 없는 경우
    if check(i, j) :
        # 6-1. 바라보는 방향을 유지한 채로 한 칸 후진
        if graph[i - dirs[dir][0]][j - dirs[dir][1]] != 1 :
            i -= dirs[dir][0]
            j -= dirs[dir][1]
        # 6-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없는 경우
        else : break
    # 7. 청소되지 않은 칸이 있는 경우
    else :
        # 7-1. 반시계 방향으로 90도 회전
        if dir == 0 : dir = 3
        else : dir -= 1
        # 7-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 경우 한 칸 전진
        if (0 <= i + dirs[dir][0] < n and 0 <= j + dirs[dir][1] < m) and not graph[i + dirs[dir][0]][j + dirs[dir][1]] :
            i += dirs[dir][0]
            j += dirs[dir][1]
# 8. 결과 출력
print(ans)
