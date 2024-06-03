import sys
input = sys.stdin.readline

# 1. 감시 체크 함수 정의
def check() :
    # 1-1.
    for x, y in teacher :
        # 1-1-1.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)] :
            for i in range(1, n) :
                nx, ny = x + dir_x * i, y + dir_y * i
                # 맵을 벗어나거나 장애물을 마주칠 경우 break
                if (nx < 0 or nx >= n or ny < 0 or ny >= n) or graph[nx][ny] == "O" : break
                # 학생이 있을 경우 False 반환
                if graph[nx][ny] == "S" : return False
    # 1-2. True 반환
    return True
# 2. 백트래킹 함수 정의
def backtracking(cnt, idx) :
    if idx == l : return
    # 2-1. 장애물이 모두 설치된 경우
    if cnt == 3 :
        # 2-1-1. 감시를 모두 피할 경우 YES 출력 후 종료
        if check() :
            print("YES")
            exit()
        return
    # 2-2.
    for i in range(idx, l) :
        x, y = empty[i]
        # 2-2-1. 장애물 설치
        graph[x][y] = "O"
        # 2-2-2. 백트래킹 실행
        backtracking(cnt + 1, i+1)
        # 2-2-3. 장애물 회수
        graph[x][y] = "X"

n = int(input())
graph = [list(input().split()) for _ in range(n)]

# 3. 선생님, 학생, 빈 곳 위치 리스트 생성
teacher, empty = [], []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == "T" : teacher.append((i, j))
        elif graph[i][j] == "X" : empty.append((i, j))
l = len(empty)
# 4. 백트래킹 실행
backtracking(0, 0)
# 5. No 출력
print("NO")