import sys
input = sys.stdin.readline

ans = int(1e9)
def solution(n, m, graph):
    global ans
    # 1. 백트래킹 함수 정의
    def backtracking(idx) :
        global ans
        # 1-1. 종료 조건 설정
        if idx == len(cctv) :
            # 최소 구역 업데이트
            cnt = 0
            for i in range(n) :
                for j in range(m) :
                    if graph[i][j] == 0 : cnt += 1
            ans = min(ans, cnt)
            return
        # 1-2.
        x, y = cctv[idx]
        for case in dirs[graph[x][y]] :
            array = []
            for (dir_x, dir_y) in case :
                # 1-2-1.
                nx, ny = -1, -1
                while True :
                    nx = nx + dir_x if nx != -1 else x + dir_x
                    ny = ny + dir_y if ny != -1 else y + dir_y
                    # 탈출 조건
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 6 : break
                    # 다음 방향이 빈 공간일 경우 # 표시 후 리스트에 삽입
                    if graph[nx][ny] == 0 :
                        graph[nx][ny] = '#'
                        array.append((nx, ny))
            # 1-2-2. 백트래킹 실행
            backtracking(idx + 1)
            # 1-2-3. 방문 제거
            for i, j in array :
                graph[i][j] = 0

    # 2. cctv 위치 리스트, 벽 개수 변수 생성
    cctv, wall = [], 0
    # 3.
    for i in range(n) :
        for j in range(m) :
            # cctv일 경우 리스트에 삽입
            if 1 <= graph[i][j] <= 5 : cctv.append((i, j))
            # 벽 개수 체크
            elif graph[i][j] == 6 : wall += 1
    # 4. 방향 변수 생성
    dirs = [[], [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]], [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]], [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
            [[(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)]], [[(-1, 0), (1, 0), (0, -1), (0, 1)]]]
    # 5. 백트래킹 실행
    backtracking(0)
    # 6. 결과 출력
    print(ans)
    
if __name__ == "__main__" :
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, graph)