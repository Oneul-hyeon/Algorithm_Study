import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(s_x, s_y) :
    # 1-1. 큐 생성 후 현재 위치 삽입
    queue = deque([(s_x, s_y)])
    # 1-2. 방문 여부 리스트 생성
    visited = [[0 for _ in range(m)] for _ in range(n)]
    # 1-3. 최대 길이 변수 생성
    max_len = 0
    # 1-4.
    while queue :
        # 1-4-1. 위치 인덱스 반환
        x, y = queue.popleft()
        # 1-4-2.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
            # 다음 위치 설정
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m or (nx, ny) == (s_x, s_y) or graph[nx][ny] == "W" : continue
            # 현재 위치에 방문하지 않은 경우
            if not visited[nx][ny] :
                # 방문 처리
                visited[nx][ny] = visited[x][y] + 1
                # 최대 길이 업데이트
                max_len = max(max_len, visited[nx][ny])
                # 큐에 다음 위치 삽입
                queue.append((nx, ny))
    # 1-5. 최대 길이 반환
    return max_len

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

# 2. 최단 거리 변수 생성
ans = -float("INF")
# 3.
for x in range(n) :
    for y in range(m) :
        # 3-1. 현재 위치가 육지인 경우
        if graph[x][y] == "L" :
            # 최단 거리 업데이트
            ans = max(ans, bfs(x, y))
# 4. 결과 출력
print(ans)