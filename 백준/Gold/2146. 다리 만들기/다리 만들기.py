import sys
from collections import deque
input = sys.stdin.readline

# 1. 섬 넘버링용 BFS 함수 정의
def bfs_numbering(x, y, number):
    # 1-1. 큐 생성 후 시작 위치 삽입
    queue = deque([(x, y)])
    # 1-2. 현재 위치 섬 번호 넘버링
    graph[x][y] = number
    # 1-3.
    while queue:
        # 위치 인덱스 반환
        x, y = queue.popleft()
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # 다음 위치 설정
            nx, ny = x+dir_x, y+dir_y
            # 예외 처리
            if nx<0 or nx>=N or ny<0 or ny>=N: continue
            # 현재 위치가 체크되지 않은 섬인 경우
            if graph[nx][ny] == 1:
                # 섬 번호 넘버링
                graph[nx][ny] = number
                # 큐에 위치 삽입
                queue.append((nx, ny))

# 2. DFS 함수 정의
def bfs_dist(x, y) :
    # 2-1. 큐 생성 후 현재 위치 삽입
    queue = deque([(x, y)])
    # 2-2. 서브 그래프 생성
    sub_graph = [[0 for _ in range(N)] for _ in range(N)]
    # 2-3.
    while queue:
        # 2-3-1. 위치 인덱스 반환
        x, y = queue.popleft()
        # 2-3-2.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # 다음 위치 설정
            nx, ny = x + dir_x, y + dir_y
            # 예외 처리
            if nx<0 or nx>=N or ny<0 or ny>=N or graph[nx][ny]==number: continue
            # 다른 섬에 도착한 경우
            if graph[nx][ny] > 0:
                # 최솟값 반환
                return sub_graph[x][y]
            # 방문하지 않은 바다일 경우
            if not sub_graph[nx][ny]:
                # 해당 위치 거리 계산
                sub_graph[nx][ny] = sub_graph[x][y] + 1
                # 큐에 다음 위치 삽입
                queue.append((nx, ny))
    # 2-4. 주변에 바다가 없다면 무한 값 반환
    return float("inf")

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 2.
number = 2
for x in range(N):
    for y in range(N):
        # 2-1. 현재 위치가 체크되지 않은 섬인 경우
        if graph[x][y] == 1:
            # bfs 실행
            bfs_numbering(x, y, number)
            # 섬 넘버링 업데이트
            number+=1

# 3,
ans = float("inf")
for x in range(N):
    for y in range(N):
        # 현재 위치가 섬인 경우
        if (number:=graph[x][y]):
            # dfs를 실행해 최소 거리 업데이트
            ans = min(ans, bfs_dist(x, y))

# 4. 최소 거리 출력
print(ans)