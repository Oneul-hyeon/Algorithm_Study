def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    # 1. 변화량 리스트 생성
    array = [[0] * (m+1) for _ in range(n+1)]
    # 2. 식에 따른 인덱스에 값 추가
    for type, r1, c1, r2, c2, degree in skill :
        if type == 1 : degree *= -1
        array[r1][c1] += degree 
        array[r1][c2+1] -= degree
        array[r2+1][c1] -= degree
        array[r2+1][c2+1] += degree
    # 3. 행 별로 이전 값에 더해주기
    for i in range(n) :
        for j in range(1, m) :
            array[i][j] += array[i][j-1]
    # 4. 열 별로 이전 값에 더해주기
    for j in range(m) :
        for i in range(1, n) :
            array[i][j] += array[i-1][j]
    # 5. 기존 건물의 내구도와 합치기
    # 6. 내구도가 1 이상인 건물 개수 체크
    for i in range(n) :
        for j in range(m) :
            board[i][j] += array[i][j]
            if board[i][j] >= 1 : answer += 1
    # 7. 결과 리턴
    return answer