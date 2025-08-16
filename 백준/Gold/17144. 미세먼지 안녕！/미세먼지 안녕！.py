import sys
input = sys.stdin.readline

# 1. 확산 함수 정의
def diffusion() -> list:
    # 1-1. 서브 그래프 생성
    sub_graph = [[0 for _ in range(C)] for _ in range(R)]
    # 1-2.
    for x in range(R) :
        for y in range(C):
            # 1-2-1. 예외처리
            if graph[x][y] == -1 : continue
            # 1-2-2. 확산되는 미세먼지 양 계산
            amount = graph[x][y] // 5
            # 1-2-3. 확산 방향 수 카운트 변수 생성
            cnt = 0
            # 1-2-4.
            for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                # 다음 방향 설정
                nx, ny = x+dir_x, y+dir_y
                # 예외 처리
                if nx<0 or nx>=R or ny<0 or ny>=C or graph[nx][ny]==-1: continue
                # 서브 그래프에 확산되는 미세먼지 추가
                sub_graph[nx][ny] += amount
                # 카운트 업데이트
                cnt += 1
            # 1-2-5. 남은 미세먼지 처리
            sub_graph[x][y] += graph[x][y] - amount*cnt
            # 1-2-6. 공기청정기 위치 마킹
            sub_graph[upper_air_purifier_x][0], sub_graph[lower_air_purifier_x][0] = -1, -1

    # 1-3. 서브 그래프 반환
    return sub_graph

# 2. 공기청정기 작동 함수 정의
def action() -> None:
    # 2-1. 위쪽 공기청정기 처리 함수 정의
    def _top_processing() -> None:
        # 2-1-1. 아래쪽 공기 이동
        graph[upper_air_purifier_x].insert(1, 0)
        mod = graph[upper_air_purifier_x].pop()
        # 2-1-2. 오른쪽 공기 이동
        for x in range(upper_air_purifier_x-1, -1, -1):
            graph[x][-1], mod = mod, graph[x][-1]
        # 2-1-3. 위쪽 공기 이동
        graph[0].insert(C-1, mod)
        mod = graph[0].pop(0)
        # 2-1-4. 왼쪽 공기 이동
        for x in range(1, upper_air_purifier_x):
            graph[x][0], mod = mod, graph[x][0]

    # 2-2. 아래쪽 공기청정기 처리 함수 정의
    def _bottom_processing() -> None:
        # 2-2-1. 위쪽 공기 이동
        graph[lower_air_purifier_x].insert(1, 0)
        mod = graph[lower_air_purifier_x].pop()
        # 2-2-2. 오른쪽 공기 이동
        for x in range(lower_air_purifier_x+1, R, 1):
            graph[x][-1], mod = mod, graph[x][-1]
        # 2-2-3. 아래쪽 공기 이동
        graph[-1].insert(C-1, mod)
        mod = graph[-1].pop(0)
        # 2-2-4. 왼쪽 공기 이동
        for x in range(R-2, lower_air_purifier_x, -1):
            graph[x][0], mod = mod, graph[x][0]

    # 2-3. 공기청정기 작동
    _top_processing()
    _bottom_processing()

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

# 3. 공기청정기 위치 구하기
upper_air_purifier_x, lower_air_purifier_x = None, None
for r in range(R) :
    if graph[r][0] == -1 :
        if upper_air_purifier_x is None :
            upper_air_purifier_x = r
        else :
            lower_air_purifier_x = r
# 4.
for _ in range(T):
    # 4-1. 미세먼지 확산
    graph = diffusion()
    # 4-2. 공기청정기 작동
    action()
# 5. 남아있는 미세먼지 양 출력
print(sum([sum(row) for row in graph]) + 2)