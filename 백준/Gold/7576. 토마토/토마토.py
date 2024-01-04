import sys
from collections import deque
input = sys.stdin.readline

def solution(n, graph):
    # 1. 큐 생성 후 초기 익은 토마토가 들어있는 인덱스 생성
    cnt = 0
    queue = deque()
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                queue.append((i, j))
            if graph[i][j] in [-1, 1] :
                cnt += 1
    if cnt == n * m :
        print(0)
    else :
        # 2.
        while queue :
            # 2-1. 큐에서 위치 반환
            x, y = queue.popleft()
            # 2-2.
            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                # 2-2-1. 다음 위치 설정
                nx, ny = x + dir_x, y + dir_y
                # 2-2-2. 예외 처리
                if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == -1 : continue
                # 2-2-3. 현재 위치가 익지 않은 토마토인 경우
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                # 2-2-4. 현재 위치에 있는 토마토가 더 빨리 익을 수 있는 경우
                elif graph[nx][ny] > graph[x][y] + 1 :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        # 3.
        ans = 0
        for i in range(n) :
            for j in range(m) :
                # 3-1. 익지 않은 토마토가 있을 경우
                if graph[i][j] == 0 :
                    print(-1)
                    exit()
                # 3-2. 최소 날짜 업데이트
                ans = max(ans, graph[i][j])
        # 4. 결과 출력
        print(ans - 1)

if __name__ == "__main__":
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution(n, graph)