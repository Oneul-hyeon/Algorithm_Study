import sys, math
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 1. 가로합 리스트 만들기
row_sum = [sum(line) for line in graph]
# 2. 세로합 리스트 만들기
col_sum = [sum(line) for line in zip(*graph)]
row_combination = list(combinations(range(n), 2))
col_combination = list(combinations(range(m), 2))
answer = -math.inf
for i1, i2 in row_combination :
    for j1, j2 in col_combination :
        duplicate = graph[i1][j1] + graph[i1][j2] + graph[i2][j1] + graph[i2][j2]
        answer = max(answer, row_sum[i1] + row_sum[i2] + col_sum[j1] + col_sum[j2] - duplicate + ((i2-i1-1)*(j2-j1-1)))
print(answer)