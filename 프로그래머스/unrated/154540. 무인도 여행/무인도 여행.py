from collections import deque
def solution(maps):
    answer = []
    # 1. BFS 함수 정의
    def bfs(x, y):
        # 1-1. 큐에 현재 위치 삽입
        queue = deque()
        queue.append((x, y))
        # 1-2. 현재 위치 방문 처리
        visited[x][y] = True
        summation = int(maps[x][y])
        # 1-3.
        while queue :
            # 위치 인덱스 반환
            x, y = queue.popleft()

            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # 다음 위치 정의
                nx, ny = x + dir_x, y + dir_y
                # 예외처리
                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                # 해당 위치가 바다가 아니면서 방문하지 않은 경우
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    # 방문 처리
                    visited[nx][ny] = True
                    # 머물 수 있는 날짜 업데이트
                    summation += int(maps[nx][ny])
                    # 큐에 다음 위치 삽입
                    queue.append((nx, ny))
        return summation

    n, m = len(maps), len(maps[0])
    # 2. 방문 여부 리스트 생성
    visited = [[False] * m for _ in range(n)]
    # 3.
    for i in range(n):
        for j in range(m):
            # 3-1. 해당 위치가 바다가 아니면서 방문하지 않은 경우
            if maps[i][j] != 'X' and not visited[i][j]:
                # bfs 실행
                answer.append(bfs(i, j))
    # 4. 결과 리턴
    return sorted(answer) if answer else [-1]