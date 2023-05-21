import sys
input = sys.stdin.readline

# 4. 재귀 함수 선언
def dfs(x, y, count, summation) :
    global max_summation
    # 5. 종료 조건 설정
    if count == 4 :
        max_summation = max(max_summation, summation)
        return
    # 6.
    for dir in dirs :
        nx, ny = x + dir[0], y + dir[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        if not visited[nx][ny] :
            # 7. 블록의 개수가 2개일 때 'ㅗ', 'ㅏ', 'ㅓ', 'ㅜ'를 위한 처리
            if count == 2 :
                visited[nx][ny] = True
                dfs(x, y, count + 1, summation + graph[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, summation + graph[nx][ny])
            visited[nx][ny] = False


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_summation = -int(1e9)
# 1. 방향 변수, 방문 여부 리스트 생성
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False for _ in range(m)] for _ in range(n)]
# 2.
for i in range(n) :
    for j in range(m) :
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
# 3. 결과 출력
print(max_summation)