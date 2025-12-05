import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 1.
virus_1, virus_2 = None, None
for x in range(N):
    for y in range(M):
        # 1-1. 인덱스 변환
        graph[x][y] = ((num:=graph[x][y]), 0)
        # 1-2. 1번, 2번 바이러스 인덱스 추출
        if num == 1:
            virus_1 = (x, y)
        elif num == 2:
            virus_2 = (x, y)
# 2. 큐 생성 후 (바이러스 번호, 1번,2번 바이러스 위치, 시간) 삽입
queue = deque([(1, *virus_1, 0), (2, *virus_2, 0)])
# 3.
while queue:
    # 3-1. 바이러스 번호, 인덱스 추출
    virus, x, y, time = queue.popleft()
    if graph[x][y][0] == 3: continue
    # 3-2.
    for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        # 3-2-1. 다음 위치 설정
        nx, ny = x+dir_x,  y+dir_y
        # 3-2-2. 예외 처리
        if nx<0 or nx>=N or ny<0 or ny>=M or graph[x][y][0] == 3 or graph[nx][ny][0] in [-1, 3]: continue
        # 3-2-3. 해당 위치에 바이러스가 없는 경우
        if not graph[nx][ny][0]:
            # 바이러스 이동
            graph[nx][ny] = (graph[x][y][0], (ntime:=time+1))
            # 큐에 다음 위치 삽입
            queue.append((graph[x][y][0], nx, ny, ntime))
        # 3-2-4.다른 바이러스가 동일한 시간에 있는 경우
        elif virus != graph[nx][ny][0] and (ntime:=time+1) == graph[nx][ny][1]:
            # 3번 바이러스로 변형
            graph[nx][ny] = (3, ntime)
# 4. 결과 출력
ans = [0 for _ in range(4)]
for x in range(N):
    for y in range(M):
        if (num:=graph[x][y][0]) > 0:
            ans[num] += 1
print(*ans[1:])