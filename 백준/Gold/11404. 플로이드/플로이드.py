import sys, math
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = math.inf
# 1. graph 변수 생성
graph = [[INF] * n for _ in range(n)]

# 2. 간선 정보 입력 받기
for i in range(n) :
    graph[i][i] = 0
for _ in range(m) :
    a, b, c = map(int,input().split())
    # 시작 도시와 도착 도시를 연결하는 도시는 하나가 아닐 수 있음
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

# 3. 점화식에 따라 graph 변수 값 설정
for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 4. 결과 출력
for a in range(n) :
    for b in range(n) :
        print(graph[a][b], end=' ') if graph[a][b] != INF else print(0, end = ' ')
    print()


