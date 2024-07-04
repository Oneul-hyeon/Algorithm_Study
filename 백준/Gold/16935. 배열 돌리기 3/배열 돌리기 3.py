import sys
input = sys.stdin.readline

# 1. 1번 연산 함수 정의
def command_1(graph) :
    # 1-1. 행/열 변경
    graph = list(zip(*graph))
    # 1-2. 좌우 반전
    graph = [line[::-1] for line in graph]
    # 1-3. 행/열 변경
    graph = list(zip(*graph))
    # 1-4. 배열 반환
    return graph

# 2. 2번 연산 함수 정의
def command_2(graph) :
    # 2-1. 좌우 반전
    graph = [line[::-1] for line in graph]
    # 2-2. 배열 반환
    return graph

# 3. 3번 연산 함수 정의
def command_3(graph, n, m) :
    # 3-1. 서브 배열 생성
    new_graph = [[0 for _ in range(n)] for _ in range(m)]
    # 3-2.
    for x in range(n) :
        for y in range(m) :
            # 3-2-1. 다음 위치 설정
            nx, ny =  y, n - x - 1
            # 3-2-2. 회전
            new_graph[nx][ny] = graph[x][y]
    # 3-3. 배열과 행/열 길이 반환
    return new_graph, m, n

# 4. 4번 연산 함수 정의
def command_4(graph, n, m) :
    # 4-1. 서브 배열 생성
    new_graph = [[0 for _ in range(n)] for _ in range(m)]
    # 4-2.
    for x in range(n) :
        for y in range(m) :
            # 4-2-1. 다음 위치 설정
            nx, ny =  m - y - 1, x
            # 4-2-2. 회전
            new_graph[nx][ny] = graph[x][y]
    # 4-3. 배열과 행/열 길이 반환
    return new_graph, m, n

# 5. 5번 연산 함수 정의
def command_5(graph, n, m) :
    size_x, size_y = n // 2, m // 2
    # 5-1. 서브 배열 생성
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    # 5-2. 1번 그룹 이동
    for x in range(size_x) :
        for y in range(size_y) :
            nx, ny = x, y + size_y
            new_graph[nx][ny] = graph[x][y]
    # 5-3. 2번 그룹 이동
    for x in range(size_x) :
        for y in range(size_y, m) :
            nx, ny = x + size_x, y
            new_graph[nx][ny] = graph[x][y]
    # 5-4. 3번 그룹 이동
    for x in range(size_x, n) :
        for y in range(size_y, m) :
            nx, ny = x, y - size_y
            new_graph[nx][ny] = graph[x][y]
    # 5-5. 4번 그룹 이동
    for x in range(size_x, n) :
        for y in range(size_y) :
            nx, ny = x - size_x, y
            new_graph[nx][ny] = graph[x][y]
    # 5-6. 배열 반환
    return new_graph

# 6. 6번 연산 함수 정의
def command_6(graph, n, m) :
    size_x, size_y = n // 2, m // 2
    # 6-1. 서브 배열 생성
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    # 6-2. 1번 그룹 이동
    for x in range(size_x) :
        for y in range(size_y) :
            nx, ny = x + size_x, y
            new_graph[nx][ny] = graph[x][y]
    # 6-3. 2번 그룹 이동
    for x in range(size_x) :
        for y in range(size_y, m) :
            nx, ny = x, y - size_y
            new_graph[nx][ny] = graph[x][y]
    # 6-4. 3번 그룹 이동
    for x in range(size_x, n) :
        for y in range(size_y, m) :
            nx, ny = x - size_x, y
            new_graph[nx][ny] = graph[x][y]
    # 6-5. 4번 그룹 이동
    for x in range(size_x, n) :
        for y in range(size_y) :
            nx, ny = x, y + size_y
            new_graph[nx][ny] = graph[x][y]
    # 6-6. 배열 반환
    return new_graph

# 7. 명령 수행 함수 정의
def process(command) :
    global n, m, graph

    # 7-1. 연산 번호에 맞는 연산 수행
    if command == 1 : graph = command_1(graph)
    elif command == 2 : graph = command_2(graph)
    elif command == 3 : graph, n, m = command_3(graph, n, m)
    elif command == 4: graph, n, m = command_4(graph, n, m)
    elif command == 5 : graph = command_5(graph, n, m)
    elif command == 6 : graph = command_6(graph, n, m)

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 8.
for command in commands :
    # 8-1. 명령 수행
    process(command)
# 9. 결과 출력
for line in graph :
    print(*line)