import sys
input = sys.stdin.readline

# 1, 재귀 함수 선언
def dfs(x, y, count, summation) :
    global max_summation
    # 2. 종료 조건 설정
    if count == k :
        # 2-1. 최댓값 비교
        if max_summation < summation :
            max_summation = summation
        return
    # 3. for문 <- 행
    for i in range(x, n) :
        # 4. for문 <- 열 : i==x일 경우에는 시작 지점을 y부터 나머지는 0부터 설정
        for j in range(y if i==x else 0, m) :
            # 4-1. 해당 위치 방문 확인
            if visited[i][j] : continue
            # 4-2. 동서남북 방향 방문 확인
            for dir in dirs :
                nx, ny = i+dir[0], j+dir[1]
                if nx<0 or nx>=n or ny<0 or ny>=m : continue
                if visited[nx][ny] : break
            # 4-3. 방문한 적이 없을 경우
            else :
                visited[i][j] = True
                dfs(i, j, count+1, summation + graph[i][j])
                visited[i][j] = False
# 5. 입력받기
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 6. 최댓값 설정
max_summation = -int(1e9)
# 7. 방문 여부 설정
visited = [[False for _ in range(m)]for _ in range(n)]
# 8. 상하좌우 방향 설정
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 9. 재귀 함수 실행
dfs(0, 0, 0, 0)
# 10. 최댓값 출력
print(max_summation)