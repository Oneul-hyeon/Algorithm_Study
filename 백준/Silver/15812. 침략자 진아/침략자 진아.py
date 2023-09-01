import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(x, y) :
    # 1-1. 현재 위치 방문 처리
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    # 1-2. 큐를 생성해 (현재 위치, 거리) 삽입
    queue = deque()
    queue.append((x, y, 0))
    # 1-3.
    while queue :
        # 1-3-1. 위치, 거리 인덱스 반환
        x, y, d = queue.popleft()
        # 1-3-2.
        for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            # 다음 위치 설정
            nx, ny = x + dir_x, y + dir_y
            # 예외처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
            # 다음 위치에 방문하지 않은 경우
            if not visited[nx][ny] :
                # 해당 위치가 마을인 경우
                if graph[nx][ny] :
                    # 시간 정보 입력
                    time[info[nx, ny]] = d + 1
                # 방문 처리
                visited[nx][ny] = True
                # 큐에 (다음 위치, 거리 + 1) 삽입
                queue.append((nx, ny, d + 1))

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# 2. 마을 정보를 딕셔너리의 키로 생성
idx = 0
info = defaultdict(list)
for i in range(n) :
    for j in range(m) :
        if graph[i][j] :
            info[i, j] = idx
            idx += 1
# 3. 마을 중독 시간 리스트 생성
times = []
# 4.
for i in range(n) :
    for j in range(m) :
        # bfs 실행
        if not graph[i][j] :
            # 해당 인덱스에서의 중독 시간 리스트 생성
            time = [0] * idx
            bfs(i, j)
            # 마을 중독 시간 리스트에 현재 인덱스에서의 중독 시간 리스트 삽입
            times.append(time)
answer = float('inf')
# 5. 최소 중독 시간 비교
for i in range(len(times)) :
    for j in range(i+1, len(times)) :
        if i != j :
            # 5-1. 두 위치에서의 중독 시간 체크
            total_time = max([min(times[i][k], times[j][k]) for k in range(idx)])
            # 5-2. 최솟값 업데이트
            answer = min(answer, total_time)
# 6. 결과 출력
print(answer)