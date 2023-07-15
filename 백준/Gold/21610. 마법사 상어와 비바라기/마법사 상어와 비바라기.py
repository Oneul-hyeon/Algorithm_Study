import sys
input = sys.stdin.readline

# 1. 구름 이동 재귀 함수 선언
def move(d, s) :
    for i in range(len(cloud)) :
        x, y = (cloud[i][0] + dirs[d][0] * s) % n, (cloud[i][1] + dirs[d][1] * s) % n
        cloud[i] = (x, y)
        basket[x][y] += 1
# 2. 물 복사 마법 재귀 함수 선언
def magic() :
    for i in range(len(cloud)) :
        count = 0
        x, y = cloud[i][0], cloud[i][1]
        for dir in [(-1, -1), (-1, 1), (1, -1), (1, 1)] :
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue
            if basket[nx][ny] : count += 1
        basket[x][y] += count

n, m = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(n)]
# 3. 방향 리스트 설정
dirs = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# 4. 구름 위치 설정
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
# 5.
for _ in range(m) :
    d, s = map(int, input().split())
    # 5-1. 구름 이동
    # 5-2. 구름 위치에 비 내리기
    move(d, s)
    # 5-3. 물 복사 마법
    magic()
    # 5-4. 구름이 있던 칸을 제외하고, 바구니에 물이 2 이상 들어있던 모든 칸을 구름 위치로 지정
    cloud = [(i, j) for i in range(n) for j in range(n) if basket[i][j] >= 2 and (i, j) not in cloud]
    # 물의 양 2씩 없애기
    for x, y in cloud :
        basket[x][y] -= 2
# 6. 결과 출력
print(sum([sum(line) for line in basket]))