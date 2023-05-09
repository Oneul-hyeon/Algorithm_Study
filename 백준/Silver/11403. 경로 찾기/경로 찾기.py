import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            if graph[a][b] == 0 :
                if graph[a][b] == 0 :
                    if graph[a][k] == 1 and graph[k][b] == 1 :
                        graph[a][b] = 1

for line in graph :
    print(*line)
