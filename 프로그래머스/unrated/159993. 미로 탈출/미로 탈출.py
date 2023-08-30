from collections import deque
def solution(maps):
    # 1. bfs 함수 정의
    def bfs(x, y, destination) :
        # 1-1. 큐에 (현재 위치, 거리) 삽입
        queue = deque()
        queue.append((x, y, 0))
        # 1-2. 방문 여부 리스트 생성
        visited = [[False] * m for _ in range(n)]
        # 1-3. 현재 위치 방문 처리
        visited[x][y] = True
        # 1-4.
        while queue :
            # 1-4-1. 위치, 거리 반환
            x, y, d = queue.popleft()
            # 1-4-2.
            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                # 다음 위치 설정
                nx, ny = x + dir_x, y + dir_y
                # 예외 처리
                if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
                # 목표 지점일 경우
                if [nx, ny] == destination : return d + 1
                # 방문하지 않은 경우
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 (다음 위치, 거리 + 1) 삽입
                    queue.append((nx, ny, d + 1))
        # 1-5. -1 반환
        return -1
    n, m = len(maps), len(maps[0])
    # 2. 시작 지점, 레버 위치, 탈출 지점 인덱스 구하기
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 'S' : start = [i, j]
            elif maps[i][j] == 'L' : lever = [i, j]
            elif maps[i][j] == 'E' : end = [i, j]
    # 3. [시작지점-레버 위치 간 거리, 레버 위치-탈출 지점 간 거리] 구하기
    distance = [bfs(start[0], start[1], lever), bfs(lever[0], lever[1], end)]
    # 4. 결과 출력
    return -1 if -1 in distance else sum(distance)