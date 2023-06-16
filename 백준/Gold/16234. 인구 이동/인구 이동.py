import sys
from collections import deque
input = sys.stdin.readline

# 5. 재귀함수 bfs 선언
def bfs(x, y, visited) :
    visited[x][y] = True
    index_lst = [(x, y)]
    queue = deque()
    queue.append((x, y))
    # 5-1. bfs를 통해 index_lst 변수에 인구이동이 발생하는 인덱스 삽입
    while queue :
        x, y = queue.popleft()
        for dir_x, dir_y in dirs :
            nx, ny = x + dir_x, y + dir_y
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if not visited[nx][ny] :
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r :
                    visited[nx][ny] = True
                    index_lst.append((nx, ny))
                    queue.append((nx, ny))
    # 5-2. 인덱스의 길이가 1일 경우(인구이동이 발생하지 않아 시작 위치만 있을 경우) True 반환
    if len(index_lst) == 1 : return True
    # 5-3. 인구이동이 발생하는 경우 주어진 식에 따라 인구 재배치
    else :
        summation = int(sum([graph[x][y] for x, y in index_lst]) / len(index_lst))
        for x, y in index_lst :
            graph[x][y] = summation
        return False

# 4. 재귀함수 check 선언
def check() :
    global ans
    # 4-1. 방문여부 변수 선언
    visited = [[False] * n for _ in range(n)]
    state = True
    # 4-2. 이중 for문을 통해 방문하지 않은 지점에서 재귀함수 bfs의 False 반환 여부 확인
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] and not bfs(i, j, visited) :
                if state : state = False
    # 4-3. 인구이동이 발생한 적이 없을 경우 True 반환
    return state

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 1. 방향 변수 설정
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
# 2.
while True :
    # 3. 재귀함수 check 실행 <- 모든 국경선이 닫혀 있는지 확인하는 재귀함수
    if check() : break
    ans += 1
print(ans)