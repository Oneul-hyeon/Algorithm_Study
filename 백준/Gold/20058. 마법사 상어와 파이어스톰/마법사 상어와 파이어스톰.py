import sys
from collections import deque
input = sys.stdin.readline

def solution(n, _, graph, command) :
    # 1. 회전 함수 정의
    def rotate(x, y, size) :
        global graph
        # 1-1. 서브 그래프 생성
        sub_graph = [line[:] for line in graph]
        # 1-2. 90도 회전
        for i in range(x, x + size) :
            for j in range(y, y+size) :
                # 1-2-1. (x, y)을 (0, 0)으로 옮겨주는 작업 수행
                ox, oy = i - x, j - y
                # 1-2-2. 변환된 위치에서 90도 이동
                rx, ry = oy, size - ox - 1
                # 1-2-3. 다시 x, y을 더해줌으로써 변동된 위치에 원래 값 입력
                graph[rx + x][ry + y] = sub_graph[i][j]

    # 2. 마법 시전 함수 정의
    def magic(x, y, size, L) :
        # 2-1. 원하는 범위에 들어왔을 경우
        if size == 2 ** L :
            # 회전 함수 실행
            rotate(x, y, size)
            return
        # 2-2. 원하는 범위에 들어오지 않았을 경우
        # size 재설정
        size //= 2
        # 분할정복
        magic(x, y, size, L)
        magic(x, y + size, size, L)
        magic(x + size, y, size, L)
        magic(x + size, y + size, size, L)
    # 3. 얼음 갯수 감소 함수 생성
    def reduction() :
        sub_graph = [line[:] for line in graph]
        # 3-1.
        for x in range(l) :
            for y in range(l) :
                if graph[x][y] == 0 : continue
                cnt = 0
                # 4방향 얼음 여부 카운트
                for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                    nx, ny = x + dir_x, y + dir_y
                    # 맵을 벗어나거나 얼음이 아닐 경우 카운트 감소
                    if nx < 0 or nx >= l or ny < 0 or ny >= l or sub_graph[nx][ny] <= 0 : continue
                    cnt += 1
                # 얼음이 있는 칸 3개 또는 그 이상과 인접해 있지 않다면 얼음의 양 감소
                if cnt < 3 : graph[x][y] -= 1
    # 4. 얼음 덩어리를 찾기 위한 bfs 함수 정의
    def bfs(x, y) :
        # 4-1. 큐 생성 후 현재 위치 삽입
        queue = deque()
        queue.append((x, y))
        # 4-2. 현재 위치 방문 처리
        visited[x][y] = True
        cnt = 1
        # 4-3.
        while queue :
            # 위치 인덱스 반환
            x, y = queue.popleft()
            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                nx, ny = x + dir_x, y + dir_y
                # 예외처리
                if nx < 0 or nx >= l or ny < 0 or ny >= l : continue
                # 얼음이 존재하면서 방문하지 않은 경우
                if graph[nx][ny] and not visited[nx][ny] :
                    # 카운팅
                    cnt += 1
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 다음 위치 삽입
                    queue.append((nx, ny))
        # 4-4. 얼음 덩어리 반환
        return cnt
    # 5. 길이 변수 생성
    l = 2 ** n
    # 6.
    for L in command :
        # 파이어스톰 실행
        magic(0, 0, l, L)
        # 얼음 갯수 줄이기
        reduction()
    # 7. 남아있는 얼음의 합 출력
    summation = sum([sum(line) for line in graph])
    print(summation)
    # 8. 가장 큰 덩어리 찾기
    max_cnt = 0
    visited = [[False for _ in range(l)] for _ in range(l)]
    for i in range(l) :
        for j in range(l) :
            if graph[i][j] and not visited[i][j] :
                cnt = bfs(i, j)
                # 최댓값 업데이트
                max_cnt = max(max_cnt, cnt)
    # 9. 가장 큰 덩어리 출력
    print(max_cnt)

if __name__ == "__main__":
    n, q = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(2**n)]
    command = list(map(int, input().split()))
    solution(n, q, graph, command)