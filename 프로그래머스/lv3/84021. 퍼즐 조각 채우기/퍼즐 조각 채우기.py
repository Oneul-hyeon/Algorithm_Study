from collections import deque

def solution(game_board, table):
    answer = 0
    def rotate(block) :
        rotate_set = [block]

        for _ in range(3) :
            block = list(map(list, zip(*block[::-1])))
            if block not in rotate_set : rotate_set.append(block)
        return rotate_set

    def return_bfs(x, y, graph, visited, state) :
        queue = deque()
        queue.append((x, y))
        block_x, block_y = [x], [y]
        visited[x][y] = True
        while queue :
            x, y = queue.popleft()
            for dir_x, dir_y in dirs :
                nx, ny = x + dir_x, y + dir_y
                if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
                if graph[nx][ny] and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    block_x.append(nx)
                    block_y.append(ny)
        block = []
        for i in range(min(block_x), max(block_x) + 1) :
            block.append(graph[i][min(block_y):max(block_y)+1])

        return (rotate(block), visited) if state else (block, visited)

    n = len(game_board)
    visited_game_board = [[False] * n for _ in range(n)]
    visited_table = [[False] * n for _ in range(n)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n) :
        for j in range(n) :
            game_board[i][j] = 0 if game_board[i][j] else 1


    board_block_set = []
    board_table_set = []
    idx = 0
    for i in range(n) :
        for j in range(n) :
            # 게임 보드의 경우
            if game_board[i][j] and not visited_game_board[i][j] :
                block, visited_game_board = return_bfs(i, j, game_board, visited_game_board, False)
                board_block_set.append(block)
            # 테이블의 경우
            if table[i][j] and not visited_table[i][j] :
                blocks, visited_table = return_bfs(i, j, table, visited_table, True)
                board_table_set.append(blocks)

    for board_block in board_block_set :
        for i in range(len(board_table_set)) :
            if board_block in board_table_set[i] :
                answer += sum([sum(line) for line in board_block])
                board_table_set.pop(i)
                break

    
    return answer