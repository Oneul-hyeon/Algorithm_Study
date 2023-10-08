import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 1. BFS 함수 정의
def bfs(graph, wall, virus) :
    # 1-1. 바이러스 위치를 큐에 삽입
    queue = deque(virus)
    # 1-2. 방문 여부 리스트 생성 후 바이러스 위치 방문 처리
    visited = [[False for _ in range(m)] for _ in range(n)]
    for x, y in virus :
        visited[x][y] = True
    # 1-3. 입력받은 벽 세우기
    for x, y in wall :
        graph[x][y] = 1
    # 1-4.
    while queue :
        x, y = queue.popleft()
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
            # 해당 위치에 방문한 적 없고 빈 공간일 경우
            if not visited[nx][ny] and not graph[nx][ny] :
                # 방문 처리
                visited[nx][ny] = True
                # 바이러스 생성
                graph[nx][ny] = 2
                # 큐에 다음 위치 삽입
                queue.append((nx, ny))
    # 1-5.
    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if not graph[i][j] : cnt += 1
    # 1-6. 빈 공간 수 반환
    return cnt

def solution(n, m, graph) :
    ans = -float("INF")
    # 2. 빈 공간, 바이러스 리스트 생성
    empty, virus = [], []
    # 3.
    for i in range(n) :
        for j in range(m) :
            # 해당 위치가 빈 공간일 경우
            if graph[i][j] == 0 : empty.append((i, j))
            # 해당 위치가 바이러스일 경우
            elif graph[i][j] == 2 : virus.append((i, j))
    # 4.
    for comb in combinations(empty, 3) :
        # BFS를 통해 안전지대 최댓값 갱신
        ans = max(ans, bfs([arr[:] for arr in graph], comb, virus))
    # 5. 결과 출력
    print(ans)

if __name__ == "__main__" :
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, graph)