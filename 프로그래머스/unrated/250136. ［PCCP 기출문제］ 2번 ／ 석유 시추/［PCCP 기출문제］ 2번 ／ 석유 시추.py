from collections import deque

def solution(land):
    # 1. BFS 함수 정의
    def bfs(x, y) :
        cnt = 0
        min_y, max_y = y, y
        # 1-1. 큐에 현재 위치 삽입
        queue = deque()
        queue.append((x, y))
        # 1-2. 현재 위치 방문 처리
        visited[x][y] = True
        # 1-4.
        while queue :
            # 1-4-1. 큐에서 정보 반환
            x, y = queue.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            # 땅 개수 카운팅
            cnt += 1
            # 1-4-2.
            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                nx, ny = x + dir_x, y + dir_y
                # 예외 처리
                if nx < 0 or nx >= n or ny < 0 or ny >= m or not land[nx][ny]: continue
                # 해당 위치가 석유가 있는 땅이면서 방문하지 않은 경우
                if not visited[nx][ny] :
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 다음 위치 삽입
                    queue.append((nx, ny))
        # 1-5. 열 별 방문한 경우 출력 리스트에 값 추가
        for j in range(min_y, max_y+1) :
            answer[j] += cnt
    
    n, m = len(land), len(land[0])
    # 2. 출력 리스트 생성
    answer = [0 for _ in range(m)]
    # 3. 방문 여부 리스트 생성
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 4. 
    for i in range(n) :
        for j in range(m) :
            # 해당 위치가 석유가 있는 땅이면서 방문하지 않은 경우 BFS 실행
            if land[i][j] == 1 and not visited[i][j] : bfs(i, j)
    # 5. 최댓값 리턴
    return max(answer)