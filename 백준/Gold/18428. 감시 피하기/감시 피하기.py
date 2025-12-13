import sys
from itertools import combinations
input = sys.stdin.readline

# 1. 체크 함수 정의
def check():
    # 1-1.
    for x, y in teacher:
        # 1-1-1.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x, y
            while True:
                # 다음 위치 정의
                nx, ny = nx+dir_x, ny+dir_y
                # 예외 처리
                if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] == "O":
                    break
                # 다음 위치에 학생이 있는 경우 False 반환
                if graph[nx][ny] == "S":
                    return False
    # 1-2. True 반환
    return True

N = int(input())
graph = [list(input().strip().split()) for _ in range(N)]

# 2. 선생님 인덱스 리스트 초기화
teacher = []
# 3. 감시 가능 인덱스 집합 초기화
potential = set()
# 4.
for x in range(N):
    for y in range(N):
        # 4-1. 해당 위치에 선생님이 있는 경우
        if graph[x][y] == "T":
            # 4-1-1. 선생님 인덱스 리스트 업데이트
            teacher.append((x, y))
            # 4-1-2.
            for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = x, y
                while True:
                    # 다음 위치 정의
                    nx, ny = nx+dir_x, ny+dir_y
                    # 예외 처리
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        break
                    # 다음 위치가 빈 칸인 경우 감시 가능 인덱스 집합 업데이트
                    if graph[nx][ny] == "X":
                        potential.add((nx, ny))
# 5.
for combination in combinations(potential, 3):
    # 5-1. 장애물 설치
    for x, y in combination:
        graph[x][y] = "O"
    # 5-2. 모든 학생이 감시를 피할 수 있다면 YES 출력 후 break
    if check():
        print("YES")
        break
    # 5-3. 장애물 해제
    for x, y in combination:
        graph[x][y] = "X"
# 6. NO 출력
else:
    print("NO")