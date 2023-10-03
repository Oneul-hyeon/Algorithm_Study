import sys
input = sys.stdin.readline

ans = 0
def solution(r, c, k, graph) :
    global ans
    # 1. DFS 함수 생성
    def dfs(x, y, d) :
        global ans
        # 1-1. 종료 조건 설정
        if d == k :
            # 현재 위치가 집인 경우
            if x == 0 and y == c - 1 : ans += 1
            return
        # 1-2.
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx < 0 or nx >= r or ny < 0 or ny >= c : continue
            # 해당 위치에 방문하지 않은 경우
            if not visited[nx][ny] and graph[nx][ny] != 'T':
                # 방문 처리
                visited[nx][ny] = True
                # DFS 실행
                dfs(nx, ny, d + 1)
                # 방문 해제
                visited[nx][ny] = False
    # 2. 방문 여부 리스트 생성
    visited = [[False for _ in range(c)] for _ in range(r)]
    # 3. 현재 위치 방문 처리
    x, y = r - 1, 0
    if graph[x][y] == '.' :
        visited[x][y] = True
        # 4. DFS 실행
        dfs(x, y, 1)
    # 5. 결과 출력
    print(ans)

if __name__ == '__main__' :
    r, c, k = map(int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(r)]
    solution(r, c, k, graph)