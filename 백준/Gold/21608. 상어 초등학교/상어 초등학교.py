import sys
input = sys.stdin.readline

n = int(input())
student = dict()
order = []
# 1. 딕셔너리에 학생의 번호 별 좋아하는 학생의 정보 입력
# 2. 리스트에 학생의 자리 배치 순서 입력
for _ in range(n**2) :
    line = list(map(int, input().split()))
    student[line[0]] = line[1:]
    order.append(line[0])
# 3. 배열 생성 <- 학생의 자리
graph = [[0 for _ in range(n)] for _ in range(n)]
# 4. 이중 for문을 동해 학생이 어디에 앉을지 선정 후 앉히기
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for who in order :
    where = []
    for x in range(n) :
        for y in range(n) :
            if graph[x][y] != 0 : continue
            like, empty = 0, 0
            for dir in dirs :
                nx, ny = x + dir[0], y + dir[1]
                if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
                # 주변에 좋아하는 학생이 얼마나 있는지
                if graph[nx][ny] in student[who] : like += 1
                # 주변에 빈 자리가 얼마나 있는지
                elif graph[nx][ny] == 0 : empty += 1
            where.append((like, empty, x, y))
    # 조건에 만족하는 칸에 학생 앉히기
    where.sort(key = lambda x : [-x[0], -x[1], x[2], x[3]])
    graph[where[0][2]][where[0][3]] = who

# 5. 이중 for문을 통해 만족도의 합 계산
satisfaction = 0
how = [0, 1, 10, 100, 1000]
for x in range(n) :
    for y in range(n) :
        count = 0
        for dir in dirs :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if graph[nx][ny] in student[graph[x][y]] : count += 1
        satisfaction += how[count]

# 6. 결과 출력
print(satisfaction)