from collections import deque

def solution(game_board, table):
    answer = 0
    # 1. bfs 함수 선언
    def return_bfs(x, y, graph, visited, state) :
        queue = deque()
        # 1-1. 큐에 현재 위치 갑입
        queue.append((x, y))
        # 1-2. 퍼증 조각이 포함되어 있는 직사각형을 구하기 위한 리스트 생성
        block_x, block_y = [x], [y]
        # 1-3. 방문 처리
        visited[x][y] = True
        # 1-4.
        while queue :
            # 큐에서 위치 인덱스 반환
            x, y = queue.popleft()
            for dir_x, dir_y in dirs :
                nx, ny = x + dir_x, y + dir_y
                # 예외 처리
                if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
                # graph 값이 1이고 방문하지 않은 경우
                if graph[nx][ny] and not visited[nx][ny] :
                    # 방문 처리
                    visited[nx][ny] = True
                    # 큐에 다음 위치 삽입
                    queue.append((nx, ny))
                    # x, y 별 리스트 삽입 
                    block_x.append(nx)
                    block_y.append(ny)
        # 1-5. 퍼즐 조각 구하기 <- 직사각형
        block = []
        for i in range(min(block_x), max(block_x) + 1) :
            block.append(graph[i][min(block_y):max(block_y)+1])
        # 1-6. game_board의 경우 빈 공간이 포함된 직사각형의 리스트 반환 / table의 경우 회전된 결과 리스트 반환
        return (rotate(block), visited) if state else (block, visited)
    
    # 2. rotate 함수 선언
    def rotate(block) :
        rotate_set = [block]
        # 2-1.
        for _ in range(3) :
            # 퍼즐 조각을 90도 회전시켜 리스트에 삽입
            block = list(map(list, zip(*block[::-1])))
            # 중복 제거
            # 2-2. 리스트 반환
            if block not in rotate_set : rotate_set.append(block)
        return rotate_set
    
    n = len(game_board)
    # 3. 방문 여부 리스트 생성
    visited_game_board = [[False] * n for _ in range(n)]
    visited_table = [[False] * n for _ in range(n)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 4. game_board의 값 변환
    for i in range(n) :
        for j in range(n) :
            game_board[i][j] = 0 if game_board[i][j] else 1

    # 5. 빈 공간 & 퍼즐 조각 리스트 생성
    board_block_set = []
    board_table_set = []
    # 6.
    for i in range(n) :
        for j in range(n) :
            # game_board의 경우
            if game_board[i][j] and not visited_game_board[i][j] :
                block, visited_game_board = return_bfs(i, j, game_board, visited_game_board, False)
                board_block_set.append(block)
            # table의 경우
            if table[i][j] and not visited_table[i][j] :
                blocks, visited_table = return_bfs(i, j, table, visited_table, True)
                board_table_set.append(blocks)
    # 7. 빈 공간에 퍼즐 조각이 들어갈 수 있는지 체크
    for board_block in board_block_set :
        for i in range(len(board_table_set)) :
            # 들어갈 수 있는 경우 채워지는 공간 수 더하기
            if board_block in board_table_set[i] :
                answer += sum([sum(line) for line in board_block])
                # 퍼즐 조각 인덱스 값 제거
                board_table_set.pop(i)
                break
    # 8. 결과 리턴
    return answer