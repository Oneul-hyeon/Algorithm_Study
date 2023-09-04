import sys
input = sys.stdin.readline

# 1. 게임 종료 함수 정의
def end_game() :
    # 1-1. 결과 출력
    print(f'kraj {idx}')
    # 1-2. 시스템 종료
    exit()
# 2. 종수 이동 함수 정의
def move_jongsoo(dir) :
    global jongsoo
    next_jongsoo = [jongsoo[0] + dirs[dir][0], jongsoo[1] + dirs[dir][1]]
    # 2-1. 이동 방향에 아두이노가 있을 경우
    if board[next_jongsoo[0]][next_jongsoo[1]] == 'R': end_game() # 게임 종료 함수 실행
    # 2-2. 보드 변환
    board[jongsoo[0]][jongsoo[1]], board[next_jongsoo[0]][next_jongsoo[1]] = '.', 'I'
    # 2-3. 종수 위치 인덱스 재설정
    jongsoo = next_jongsoo
    return

# 3. 미친 아두이노 이동 함수 정의
def craze_arduino(x, y) :
    global arduino
    # 3-1. 최소 거리를 갖는 방향 찾기
    distance = [float('inf')]
    for dir_x, dir_y in dirs[1:] :
        nx, ny = x + dir_x, y + dir_y
        distance.append(abs(jongsoo[0] - nx) + abs(jongsoo[1] - ny))
    best_dir = distance.index(min(distance))
    nx, ny = x + dirs[best_dir][0], y + dirs[best_dir][1]
    # 3-2. 아두이노 이동에 따른 보드 위치 재설정
    if board[x][y] == 'R' : board[x][y] = '.' # 현재 위치가 R일 경우
    elif board[x][y][:-1] == 'R' : board[x][y] = 'R' # 현재 위치가 RR 일 경우
    # 3-3. 다음 위치가 종수 위치일 경우 종료
    if board[nx][ny] == 'I' :
        end_game()
    # 3-4. 다음 위치가 빈 칸일 경우
    elif board[nx][ny] == '.' :
        board[nx][ny] = 'R'
    # 3-5. 아두이노 위치일 경우
    else :
        board[nx][ny] += 'R'
    return

r, c = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(r)]
# 4. 이동 방향 리스트 정의
dirs = [[], (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
# 5. 종수 이동방향 리스트화
order = [0] + list(map(int, input().rstrip()))
# 6. 종수 위치와 아두이노 위치 구하기
arduino = []
for i in range(r) :
    for j in range(c) :
        # 종수 위치일 경우
        if board[i][j] == 'I' : jongsoo = [i, j]
        # 아두이노일 경우
        elif board[i][j] == 'R' : arduino.append([i, j])
# 7.
for idx, dir in enumerate(order) :
    if idx == 0 : continue
    # 7-1. 종수 이동
    move_jongsoo(dir)
    # 7-2.
    for x, y in arduino :
        # 미친 아두이노 이동 함수 실행
        craze_arduino(x, y)
    # 7-3. 아두이노 위치 재설정
    sub_arduino = []
    for i in range(r):
        for j in range(c):
            # 해당 인덱스에 아두이노 개수가 2개 이상일 경우 아두이노 파괴
            if len(board[i][j]) >= 2: board[i][j] = '.'
            # 아두이노가 1개만 있을 경우 다음 아두이노 위치 리스트에 저장
            elif board[i][j] == 'R' : sub_arduino.append([i, j])
    arduino = sub_arduino.copy()

# 8. 보드 출력
for line in board :
    print(''.join(line))