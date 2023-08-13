import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(x, y, chance) :
    # 1-1. 거리 계산 리스트 생성
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    # 1-2. 현재 위치 거리 처리
    visited[x][y][chance] = 1
    # 1-3. 큐에 (현재 위치, 벽을 부술 기회) 삽입
    queue = deque([(x, y, chance)])
    # 1-4.
    while queue :
        # 1-4-1. 위치, 기회 반환
        x, y, chance = queue.popleft()
        # 1-4-2. 종료 조건 설정
        if x == n-1 and y == m-1 : return visited[x][y][chance]
        # 1-4-3.
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
            # 기회가 있고 해당 위치가 벽인 경우
            if chance and graph[nx][ny] :
                # 해당 위치 거리 정보 저장
                visited[nx][ny][0] = visited[x][y][chance] + 1
                # 큐에 (다음 위치, 기회) 삽입
                queue.append((nx, ny, 0))
            # 해당 위치가 벽이 아닌 경우
            if not graph[nx][ny] and not visited[nx][ny][chance] :
                # 해당 위치 거리 정보 저장
                visited[nx][ny][chance] = visited[x][y][chance] + 1
                # 큐에 (다음 위치, 기회) 삽입
                queue.append(((nx, ny, chance)))
    # 도달하지 못한 경우 -1 반환
    return -1

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# 2. bfs 실행
ans = bfs(0, 0, 1)
# 3. 결과 출력
print(ans)