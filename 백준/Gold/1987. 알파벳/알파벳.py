import sys
input = sys.stdin.readline

# 1. dfs 함수 정의
def dfs(x, y, string) :
    global max_len
    # 1-1.
    for dir_x, dir_y in dirs :
        nx, ny = x + dir_x, y + dir_y

        # 예외처리
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        # 방문한 적이 있는 경우 최댓값 업데이트
        if visited[nx][ny] : max_len = max(max_len, len(string))
        # 방문한 적이 없는 경우
        else :
            # 해당 문자가 문자열에 이미 있는 경우 최댓값 업데이트
            if board[nx][ny] in string : max_len = max(max_len, len(string))
            # 해당 문자가 문자열에 없는 경우
            else :
                # 방문 처리
                visited[nx][ny] = True
                # dfs 실행
                dfs(nx, ny, string + board[nx][ny])
                # 방문 취소
                visited[nx][ny] = False
                
n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
string = board[0][0]
max_len = -int(1e9)
# 2. 방문 여부 리스트 생성
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
# 3. dfs 실행
dfs(0, 0, string)
# 4. 결과 출력
print(max_len)