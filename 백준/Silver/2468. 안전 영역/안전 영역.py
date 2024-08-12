import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(x, y) :
    # 1-1. 큐 생성 후 현재 위치 삽입
    queue = deque([(x, y)])
    # 1-2. 현재 위치 방문 처리
    visited[x][y] = True
    # 1-3.
    while queue :
        # 1-3-1. 위치 인덱스 반환
        x, y = queue.popleft()
        # 1-3-2.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
            # 다음 위치 설정
            nx, ny = x + dir_x, y + dir_y
            # 맵을 벗어나거나 다음 높이가 기준 높이 이하이거나 이미 방문한 경우 예외처리
            if (nx < 0 or nx >= n or ny < 0 or ny >= n) or graph[nx][ny] <= height or visited[nx][ny] : continue
            # 방문 처리
            visited[nx][ny] = True
            # 큐에 다음 위치 삽입
            queue.append((nx, ny))
    # 1-4. 1 리턴
    return 1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 1

# 2. 그래프 내 중복 제거된 높이 리스트 생성
heights = set()
for row in graph :
    heights |= set(row)
# 3.
for height in sorted(list(heights)) :
    # 3-1. 방문 여부 리스트 생성
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    # 3-2.
    for i in range(n) :
        for j in range(n) :
            # 3-2-1. 현재 위치의 높이가 물에 잠기지 않으면서 방문한 적 없는 경우
            if graph[i][j] > height and not visited[i][j] :
                # bfs 실행
                # 안전한 영역 수 업데이트
                count += bfs(i, j)
    # 3-3. 안전한 영역의 최댓값 업데이트
    ans = max(ans, count)
# 4. 결과 출력
print(ans)