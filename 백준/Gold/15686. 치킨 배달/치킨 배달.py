import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
home, chicken = [], []

# 집, 치킨 집 위치 찾기
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            home.append((i, j))
        elif graph[i][j] == 2 :
            chicken.append((i, j))

# 살려둘 치킨집 인덱스 구하기
combination = combinations(range(len(chicken)), m)

min_ans = int(1e9)
for com in combination :
    ans = 0
    for x, y in home :
        ans += min([abs(x - chicken[i][0]) + abs(y - chicken[i][1]) for i in com])
    min_ans = min(min_ans, ans)

print(min_ans)