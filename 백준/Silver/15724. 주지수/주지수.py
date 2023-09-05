import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0 for _ in range(m+1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]
# 1. 누적합 배열 생성
prefix_sum = graph.copy()
# 2. 누적합 생성
for i in range(1, n + 1) :
    for j in range(1, m + 1) :
        prefix_sum[i][j] += prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        
t = int(input())
for _ in range(t) :
    x1, y1, x2, y2 = map(int, input().split())
    # 3. 점화식에 따른 사람 수의 합 출력
    print(prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + graph[x1-1][y1-1])