import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(n, graph) :
    # 1. bfs 함수 정의
    def bfs(x, y) :
        # 1-1. bfs를 위한 graph 생성
        bfs_graph = [[float('inf') for _ in range(n)] for _ in range(n)]
        # 1-2. 현재 위치 큐에 삽입 후 거리를 0으로 설정
        queue = deque()
        queue.append((x, y))
        bfs_graph[x][y] = 0
        # 1-3.
        while queue :
            x, y = queue.popleft()
            for dir_x, dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                nx, ny = x + dir_x, y + dir_y
                # 예외 처리
                if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
                # 해당 위치의 물고기의 무게가 아기 상어의 몸무게보다 작거나 같을 경우
                if baby_shark >= graph[nx][ny] :
                    # 현재 위치에서 이동하는 경우가 더 짧은 거리일 경우
                    if bfs_graph[nx][ny] > bfs_graph[x][y] + 1 :
                        # 거리 업데이트
                        bfs_graph[nx][ny] = bfs_graph[x][y] + 1
                        # 큐에 다음 위치 삽입
                        queue.append((nx, ny))
        # 1-4. 거리 정보 반환
        return bfs_graph

    # 2. 현재 조건에 맞는 물고기 인덱스 체크 함수 정의
    def check(x, y, possible) :
        # 2-1. 딕셔너리 생성
        distance = defaultdict(list)
        # 2-2. 물고기 별 거리 계산
        bfs_graph = bfs(x, y)
        for fish in possible :
            distance[bfs_graph[fish[0]][fish[1]]].append(fish)
        # 2-3. 최소 거리의 물고리 위치 리스트 추출
        min_distance = sorted(list(distance.keys()))[0]
        fishes = sorted(distance[min_distance])
        # 2-4. 최종 물고기 인덱스, 거리 반환
        return fishes[0][0], fishes[0][1], min_distance

    # 3. 무게 별 물고기 위치 저장
    weight = defaultdict(list)
    for i in range(n) :
        for j in range(n) :
            # 아기 상어 위치 저장
            if graph[i][j] == 9 :
                x, y = i, j
                graph[i][j] = 0
            # 물고기 위치 저장
            elif graph[i][j] : weight[graph[i][j]].append([i, j])
    # 4.
    baby_shark = 2 # 아기 상어의 현재 크기
    possible = []
    time = 0
    while True :
        # 4-1. 현재 먹을 수 있는 물고기 리스트 생성
        possible.extend(weight[baby_shark - 1].copy())
        # 4-2.
        for _ in range(baby_shark) :
            # 4-2-1. 종료 조건 설정
            if not possible :
                print(time)
                exit()
            # 4-2-2. 조건에 맞는 물고기 인덱스 체크
            fish_x, fish_y, t = check(x, y, possible)
            if t == float('inf') :
                print(time)
                exit()
            # 4-2-3. 시간 업데이트
            time += t
            # 4-2-4. 먹은 물고기는 리스트에서 제거
            possible.remove([fish_x, fish_y])
            # 4-2-5. 상어 위치 업데이트
            x, y = fish_x, fish_y
        # 4-3. 상어 크기 증가
        baby_shark += 1

if __name__ == '__main__' :
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution(n, graph)