import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(caw1, caw2) :
    # 1-1. 방문 여부 리스트 생성
    visited = [[False] * (n+1) for _ in range(n+1)]
    # 1-2. 큐에 첫 번째 소의 위치 삽입
    queue = deque()
    queue.append((caw1[0], caw1[1]))
    # 1-3. 첫 번째 소의 위치 방문 처리
    visited[caw1[0]][caw1[1]] = True
    # 1-4.
    while queue :
        # 큐에서 위치 인덱스 반환
        x, y = queue.popleft()
        for dir_x, dir_y in dirs :
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx <= 0 or nx > n or ny <= 0 or ny > n : continue  # 범위를 벗어난 경우
            if (nx, ny) in roads[x][y] : continue   # 길이 있는 경우
            # 다음 위치를 방문하지 않은 경우
            if not visited[nx][ny] :
                # 방문 처리
                visited[nx][ny] = True
                # 큐에 다음 위치 삽입
                queue.append((nx, ny))
    # 1-5. 길을 건너도 되지 않는 경우 0, 길을 건너야 하는 경우 1 반환
    return 0 if visited[caw2[0]][caw2[1]] else 1

n, k, r = map(int, input().split())
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
# 2. 길 정보 입력하기
roads = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r) :
    x1, y1, x2, y2 = map(int, input().split())
    roads[x1][y1].append((x2, y2))
    roads[x2][y2].append((x1, y1))
# 3. 소 위치 리스트 생성
caws = [list(map(int, input().split())) for _ in range(k)]
# 4.
for i in range(k) :
    for j in range(i+1, k) :
        # 4-1. bfs를 실행해 길을 건너는지 여부 확인
        ans += bfs(caws[i], caws[j])
# 5. 결과 출력
print(ans)