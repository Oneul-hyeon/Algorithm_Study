import sys

# 1. dfs 함수 정의
def dfs(x, y, string, count) :
    global ans
    # 1-1. 종료 조건 설정
    if count == 6 :
        # 중복이 안 될 시 카운팅
        if string not in ans :
            ans.append(string)
        return
    # 1-2.
    for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
        # 다음 위치 설정
        nx, ny = x + dir_x, y + dir_y
        # 예외 처리
        if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
        # dfs 실행
        dfs(nx, ny, string + graph[nx][ny], count + 1)

n = 5
ans = []
graph = [list(map(str, input().rstrip().split())) for _ in range(n)]
# 2.
for i in range(n) :
    for j in range(n) :
        # 2-1. dfs 실행
        dfs(i, j, graph[i][j], 1)
# 3. 결과 출력
print(len(ans))