import sys
from collections import deque
input = sys.stdin.readline

dir = 1
N, K = int(input()), int(input())
# 1. 사과 정보 입력
apple = [[False for _ in range(N+1)] for _ in range(N+1)]
for _ in range(K):
    x, y = map(int, input().split())
    apple[x][y] = True
# 2. 뱀 방향 변환 리스트 생성
direction_change_information = []
for _ in range(int(input())):
    X, C = map(str, input().strip().split())
    direction_change_information.append((int(X), C))
# 3. 방향 리스트 생성
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 4. 뱀 위치 딕셔너리 생성 및 초기값 설정
snake_info = {(1, 1): True}
# 5. 큐에 초기 뱀 위치 삽입
snake = deque([(1, 1)])
# 6. 시간 정보 초기화
time = 0
# 7.
while True:
    # 7-1. 시간 정보 업데이트
    time += 1
    # 7-2. 다음 시간의 뱀 머리 위치 추출
    nx, ny = snake[0][0] + dirs[dir][0], snake[0][1] + dirs[dir][1]
    # 7-3. 이동한 위치가 벽이거나 자기 자신이라면 while문 탈출
    if nx < 1 or nx > N or ny < 1 or ny > N or (nx, ny) in snake_info: break
    # 7-4. 이외의 경우 뱀 위치 정보 업데이트
    else :
        snake_info[(nx, ny)] = True
        snake.appendleft((nx, ny))
    # 7-5. 이동한 위치에 사과가 있는 경우 사과 정보 제거
    if apple[nx][ny]:
        apple[nx][ny] = False
    # 7-6. 이동한 위치에 사과가 없는 경우
    else:
        # 7-6-1. 꼬리 이동
        tx, ty = snake.pop()
        del snake_info[(tx, ty)]
    # 7-7. 뱀의 방향 변환 체크 및 처리
    if direction_change_information and direction_change_information[0][0] == time:
        dir = (dir+1) % 4 if (C:=direction_change_information.pop(0)[1]) == "D" else (dir-1) % 4
# 8. 결과 출력
print(time)