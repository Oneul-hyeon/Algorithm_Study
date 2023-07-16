import sys, math
input = sys.stdin.readline
INF = math.inf
xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

graph = [[INF for _ in range(8)] for _ in range(8)]
# 자기 자신에서 자기 자신으로 가는 비용 초기화
for i in range(8) :
    graph[i][i] = 0
# 인덱스 정보 입력
# 시작점 인덱스 : 0, 끝점 인덱스 : 7
dic = {}
dic[0], dic[7] = (xs, ys), (xe, ye)
i = 1
# 간선 정보 입력받기
for _ in range(3):
    s1, e1, s2, e2 = map(int, input().split())
    dic[i], dic[i+1] = (s1, e1), (s2, e2)
    graph[i][i+1] = min(10, abs((s2 - s1)) + abs((e2 - e1)))
    graph[i+1][i] = min(10, abs((s2 - s1)) + abs((e2 - e1)))
    i+=2

for i in range(8) :
    for j in range(8) :
        if graph[i][j] == INF :
            graph[i][j] = abs(dic[i][0] - dic[j][0]) + abs(dic[i][1] - dic[j][1])

# 플루이드-워셜 알고리즘 수행
graph[0][7], graph[7][0] = abs((xe - xs)) + abs((ye - ys)), abs((xe - xs)) + abs((ye - ys))
for k in range(8) :
    for i in range(8) :
        for j in range(8) :
            if i!=j :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 시작점 인덱스 : 0, 끝점 인덱스 : 7
print(graph[0][7])
