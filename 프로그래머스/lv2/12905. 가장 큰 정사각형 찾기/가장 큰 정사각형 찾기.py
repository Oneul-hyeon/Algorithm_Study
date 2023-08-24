def solution(board):
    # 1. 표의 행, 열 길이 구하기
    n, m = len(board), len(board[0])
    max_l = max(board[0])
    # 2.
    for i in range(1, n) :
        for j in range(1, m) :
            if board[i][j] :
                # 2-1. 점화식에 따라 처리
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                # 2-2. 최대 변 길이 업데이트
                max_l = max(max_l, board[i][j])
    # 3. 넓이 리턴
    return max_l * max_l