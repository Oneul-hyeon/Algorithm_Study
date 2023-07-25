import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
campus = [list(map(str, input().rstrip())) for _ in range(n)]
ans = 0
# 1. 도연이의 위치 인덱스 구하기
for i in range(n) :
    for j in range(m) :
        if campus[i][j] == 'I' : x, y = i, j; break
    else : continue
    break
# 2. 방문 여부 리스트 생성
visited = [[False] * m for _ in range(n)]
# 3. 큐에 도연이 위치 삽입
queue = deque()
queue.append((x, y))
# 4. 방문 처리
visited[x][y] = True
# 5.
while queue :
    # 5-1. 큐에서 위치 인덱스 반환
    x, y = queue.popleft()
    for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
        nx, ny = x + dir_x, y + dir_y
        # 예외처리
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        # 다음 위치에 방문하지 않고 벽이 아닌 경우
        if not visited[nx][ny] and campus[nx][ny] != 'X':
            # 방문 처리
            visited[nx][ny] = True
            # 다음 위치가 사람일 경우 카운트
            if campus[nx][ny] == 'P' : ans += 1
            # 큐에 다음 위치 삽입
            queue.append((nx, ny))
# 6. 결과 출력
print(ans) if ans else print('TT')