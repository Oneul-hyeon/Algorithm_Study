import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 선언
def bfs(x, y) :
    # 1-1. 큐에 현재 위치 삽입
    queue = deque()
    queue.append((x, y, 0))
    # 1-2. 방문 여부 리스트 생성
    visited = [[False] * m for _ in range(n)]
    # 1-3. 방문 처리
    visited[x][y] = True
    # 1-4.
    while queue :
        # 1-4-1. 위치 인덱스 반환
        x, y, count = queue.popleft()
        # 1-4-2.
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] :
            # 다음 위치 설정
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
            # 해당 위치 도달 최솟값 업데이트
            if not visited[nx][ny] and graph[nx][ny] == 0 :
                visited[nx][ny] = True
                distance[nx][ny] = min(distance[nx][ny], count + 1)
                queue.append((nx, ny, count + 1))
    return
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[sys.maxsize] * m for _ in range(n)]
# 2. 상어 위치 인덱스 추출
sharks = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] : sharks.append([i, j])
# 3.
for i, j in sharks :
    # 3-1. bfs 실행
    bfs(i, j)

# 4. 결과 출력
ans = -sys.maxsize
for i in range(n) :
    for j in range(m) :
        if distance[i][j] != sys.maxsize :
            ans = max(ans, distance[i][j])
print(ans)