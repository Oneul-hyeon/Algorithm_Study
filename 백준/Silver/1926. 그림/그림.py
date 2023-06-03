import sys
from collections import deque
input = sys.stdin.readline

# 6. bfs함수 선언
def bfs(x, y) :
    global max_area
    # 7. 큐 생성
    queue = deque()
    # 8. 큐에 현재 위치 append
    queue.append((x, y))
    visited[x][y] = True
    area = 1
    # 9.
    while queue :
        # 10. 위치 반환
        x, y = queue.popleft()
        # 11.
        for i in range(4) :
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            # 12. 다음 위치가 범위를 벗어나는 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
            if graph[nx][ny] and not visited[nx][ny] :
                visited[nx][ny] = True
                area += 1
                graph[nx][ny] = area
                # 13. 최대 넓이 갱신
                max_area = max(max_area, area)
                # 14. 방문 처리 후 다음 위치 큐에 삽입
                queue.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 1. 방문 여부 리스트 생성
visited = [[False] * m for _ in range(n)]
# 2 .그림의 개수, 최대 넓이 변수 생성
count, max_area = 0, 0
# 3.
for i in range(n) :
    for j in range(m) :
        # 4. 해당 위치 값이 1이면서 방문한 적이 없을 경우 bfs 함수 실행
        if graph[i][j] and not visited[i][j] :
            bfs(i, j)
            count += 1
if count and not max_area : max_area = 1
# 5. 결과 출력
print(f'{count}\n{max_area}')