import sys
input = sys.stdin.readline

# 1. 스도쿠 행 체크 함수
def check_row(x, num) :
    if num in sudoku[x] : return False
    return True
# 2. 스도쿠 열 체크 함수
def check_col(y, num) :
    for i in range(9) :
        if sudoku[i][y] == num : return False
    return True
# 3. 3x3 정사각형 체크 함수
def check_squre(x, y, num) :
    for i in range(x//3 * 3, x//3 * 3 + 3) :
        for j in range(y//3 * 3, y//3 * 3 + 3) :
            if sudoku[i][j] == num : return False
    return True
# 5. 백트래킹 함수 정의
def backtracking(n) :
    # 5-1. 종료 조건 설정
    if n == len(blank) :
        # 모든 빈 칸을 다 채운 경우이므로 스토쿠 출력 후 시스템 종료
        for line in sudoku :
            print(*line)
        exit()
    # 5-2. 빈 칸의 인덱스 가져오기
    x, y = blank[n]
    # 5-3.
    for num in range(1, 10) :
        # 현재 인덱스에 해당 수 설정이 가능할 경우
        if check_row(x, num) and check_col(y, num) and check_squre(x, y, num) :
            # 현재 인덱스에 스도쿠 작성
            sudoku[x][y] = num
            # 백트래킹 함수 실행
            backtracking(n+1)
            # 현재 인덱스 빈 칸 처리
            sudoku[x][y] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
# 6. 빈 칸 인덱스 리스트 생성
blank = []
for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 : blank.append((i, j))
# 7. 백트래킹 함수 실행
backtracking(0)