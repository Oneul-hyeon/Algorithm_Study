import sys
from collections import deque
input = sys.stdin.readline

def solution(m, n, graph) :
    # 1. bfs 함수 정의
    def bfs(x, y) :
        # 1-1. 현재 위치 큐에 삽입
        queue = deque()
        queue.append((x, y))
        # 1-2. 현재 위치 방문 처리
        visited[x][y] = True
        # 1-3.
        while queue :
            # 위치 인덱스 반환
            x, y = queue.popleft()
            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                # 다음 위치 정의
                nx, ny = x + dir_x, y + dir_y
                # 예외 처리
                if nx < 0 or nx >= m or ny < 0 or ny >= n : continue
                # 해당 위치가 벽이 아니면서 방문하지 않은 경우
                if not graph[nx][ny] and not visited[nx][ny] :
                    # 다음 위치가 마지막 해일 경우 YES 반환 후 시스템 종료
                    if nx == m - 1 :
                        print('YES')
                        exit()
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 다음 위치 삽입
                    queue.append((nx, ny))
    # 2. 방문 여부 리스트 생성
    visited = [[False] * n for _ in range(m)]
    # 3.
    for j in range(n) :
        # 3-1. 해당 열이 빈 공간이면서 방문 처리가 안 된 경우
        if not graph[0][j] and not visited[0][j] :
            # bfs 실행
            bfs(0, j)
    # 4. NO 출력
    print('NO')

if __name__ == "__main__" :
    m, n = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(m)]
    solution(m, n, graph)