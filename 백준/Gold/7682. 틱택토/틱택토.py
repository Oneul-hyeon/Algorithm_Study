import sys
input = sys.stdin.readline

# 1. 게임 유효성 검사 함수 정의
def game_validation(board) :
    # 1-1. 말 수 체크 함수 정의
    def check_piece() :
        # 1-1-1. 각 말의 수 반환
        piece = {"X" : 0, "O" : 0}
        for i in range(3) :
            for j in range(3) :
                if board[i][j] == "." : continue
                piece[board[i][j]] += 1
        return piece["X"], piece["O"]
    # 1-2. 빙고 체크 함수 정의
    def check_bingo() :
        # 1-2-1. 가로 빙고 체크
        bingo = {"X" : 0, "O" : 0}
        for row in board :
            if len(line := list(set(row))) == 1 and line[0] != "." : bingo[line[0]] += 1
        # 1-2-2. 세로 빙고 체크
        for col in zip(*board) :
            if len(line := list(set(list(col)))) == 1 and line[0] != "." : bingo[line[0]] += 1
        # 1-2-3. 대각선 빙고 체크
        if len(line := list(set([board[0][0], board[1][1], board[2][2]]))) == 1 and line[0] != "." : bingo[line[0]] += 1
        if len(line := list(set([board[0][2], board[1][1], board[2][0]]))) == 1 and line[0] != "." : bingo[line[0]] += 1
        # 1-2-4. 말 별 빙고 수 반환
        return bingo["X"], bingo["O"]
    # 1-3. 게임판 생성
    board = [list(board[:3]), list(board[3:6]), list(board[6:])]
    # 1-4. 말 수 반환
    piece_x, piece_o = check_piece()
    # 1-5. 말 별 빙고 수 반환
    bingo_x, bingo_o = check_bingo()
    # 1-6. 빙고가 없으면서 게임판이 가득찬 경우 valid 반환
    if not bingo_x and not bingo_o :
        if piece_x == 5 and piece_o == 4 : return "valid"
    # 1-7. X만 빙고인 경우
    elif bingo_x <= 2 and not bingo_o :
        # 1-7-1. X 말의 수가 O 말의 수보다 1개 더 많은 경우 valid 반환
        if piece_x - 1 == piece_o : return "valid"
    # 1-8. O만 빙고인 경우
    elif not bingo_x and bingo_o == 1 :
        # 1-8-1. X 말의 수와 O 말의 수가 같을 경우 valid 반환
        if piece_x == piece_o : return "valid"
    # 1-9. 이외의 경우 invalid 반환
    return "invalid"
# 2.
while (board := input().strip()) != "end" :
    # 2-1. 게임 유효성 검사 실행
    print(game_validation(board))