import sys
input = sys.stdin.readline

def solution(n, m, graph, x, y) :
    # 1. 방향 재설정 함수 정의
    def next_direction(planet, direction) :
        # 1-1. 현재 방향이 U 일 경우
        if direction == 'U' : return 'R' if planet == '/' else 'L'
        # 1-2. 현재 방향이 R 일 경우
        elif direction == 'R' : return 'U' if planet == '/' else 'D'
        # 1-3. 현재 방향이 D 일 경우
        elif direction == 'D' : return 'L' if planet == '/' else 'R'
        # 1-4. 현재 방향이 L 일 경우
        else : return 'D' if planet == '/' else 'U'
    # 2. 시그널 유지 시간 함수 정의
    def return_time(direction) :
        # 2-1. 초기 위치 설정
        nx, ny = x, y
        # 2-2. 이전 경로 그래프 생성
        prior_graph = [[[] for _ in range(m)] for _ in range(n)]
        # 2-3.
        time = 0
        while True :
            # 2-3-1. 다음 위치 정의
            nnx, nny = nx + dirs[direction][0], ny + dirs[direction][1]
            # 2-3-2. 시간 카운팅
            time += 1
            # 2-3-3. 탈출 조건 설정
            if (nnx < 0 or nnx >= n or nny < 0 or nny >= m) or (graph[nnx][nny] == 'C') : break
            # 2-3-4. 현재 위치가 이전 위치에서 온 적 있는 경우
            if (nx, ny) in prior_graph[nnx][nny] :
                return 'Voyager'
            # 2-3-5. 이전 정보 삽입
            prior_graph[nnx][nny].append((nx, ny))
            # 2-3-6. 현재 위치가 행성일 경우 방향 변환
            if graph[nnx][nny] != '.' : direction = next_direction(graph[nnx][nny], direction)
            # 2-3-7. 현재 위치 업데이트
            nx, ny = nnx, nny
        # 2-4. 소요 시간 반환
        return time
    if graph[x][y] == 'C' :
        print('U')
        print(0)
    else :
        # 3. 방향 변수 생성
        dirs = {'U' : (-1, 0), 'R' : (0, 1), 'D' : (1, 0), 'L' : (0, -1)}
        # 4. 최종 방향, 시간 함수 정의
        ans_dir, ans_time = '', 0
        for direction in ['U', 'R', 'D', 'L'] :
            t = return_time(direction)
            if t == 'Voyager' or t > ans_time :
                # 방향, 시간 업데이트
                ans_dir, ans_time = direction, t
                if t == 'Voyager' : break
        # 5. 결과 출력
        print(ans_dir)
        print(ans_time)
        
if __name__ == "__main__" :
    n, m = map(int, input().split())
    graph = [input().rstrip() for _ in range(n)]
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    solution(n, m, graph, x, y)