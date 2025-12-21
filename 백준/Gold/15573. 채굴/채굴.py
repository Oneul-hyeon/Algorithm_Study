import sys
from collections import deque
input = sys.stdin.readline

# 1. BFS 함수 정의
def BFS(D:int) -> int:
    # 1-1. 현재 공기와 맞닿아 있는 광물 중 채굴 가능한 인덱스 추출
    indexs = [item for key, value in outline_info.items() for item in value if key <= D]
    # 1-2. 큐 생성 후 해당 인덱스 삽입
    queue = deque(indexs)
    # 1-3. 방문 여부 리스트 생성 후 해당 인덱스 방문 처리
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x, y in indexs:
        visited[x][y] = True
    # 1-4. 채굴 광물 수 초기화
    cnt = len(indexs)
    # 1-5.
    while queue:
        # 1-5-1. 큐에서 인덱스 추출
        x, y = queue.popleft()
        # 1-5-2.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # 다음 위치 설정
            nx, ny = x+dir_x, y+dir_y
            # 예외 처리
            if nx<0 or nx>=N or ny<0 or ny>=M : continue
            # 다음 위치에 방문하지 않았으면서, 채굴 가능한 경우
            if not visited[nx][ny] and graph[nx][ny] <= D:
                # 방문 처리
                visited[nx][ny] = True
                # 큐에 다음 인덱스 삽입
                queue.append((nx, ny))
                # 채굴 광물 수 업데이트
                cnt += 1
    # 1-6. 채굴 광물 수 반환
    return cnt

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 2. 초기 테두리 광물 정보 딕셔너리 생성
outline_info = dict()
for y in range(M):
    rows = N if y==0 or y==M-1 else 1
    for x in range(rows):
        if (strength := graph[x][y]) in outline_info:
            outline_info[strength].append((x, y))
        else:
            outline_info[strength] = [(x ,y)]
# 3. 테두리 광물의 최소 강도와 최대 강도 추출
left, right = min(outline_info.keys()), max([graph[x][y] for x in range(N) for y in range(M)])
# 4.
while left <= right:
    # 4-1. 중앙 값 설정
    D = (left+right) // 2
    # 4-2. 채굴 가능한 광물 수 체크
    cnt = BFS(D)
    # 4-3. 채굴 가능한 광물 수가 목표 광물 수보다 적은 경우 left 값 업데이트
    if cnt < K:
        left = D+1
    # 4-4. 채굴 가능한 광물 수가 목표 광물 수보다 많거나 같은 경우 right 값 업데이트
    else:
        right = D-1
# 5. 결과 출력
print(left)