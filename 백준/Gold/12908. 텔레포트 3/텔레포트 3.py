import sys, math
input = sys.stdin.readline
INF = math.inf
xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

# 1. 플로이드-워셜을 위한 graph 생성
graph = [[INF for _ in range(8)] for _ in range(8)]
# 2. 자기 자신에서 자기 자신으로 가는 비용 초기화
for i in range(8) :
    graph[i][i] = 0
# 3. 인덱스 정보 입력용 딕셔너리 생성
# 시작점 인덱스 : 0, 끝점 인덱스 : 7
dic = {}
dic[0], dic[7] = (xs, ys), (xe, ye)
# 4. for문을 통해 간선 정보 입력받기
i = 1
for _ in range(3):
    s1, e1, s2, e2 = map(int, input().split())
    # 딕셔너리에 인덱스 입력
    dic[i], dic[i+1] = (s1, e1), (s2, e2)
    # graph에 점프 이동, 텔레포트 이동 중 작은 값 입력
    jump = abs((s2 - s1)) + abs((e2 - e1))
    graph[i][i+1] = min(10, jump)
    graph[i+1][i] = min(10, jump)
    i+=2

# 5. 텔레포트가 불가능한 지역은 점프로 이동하는 거리 입력
for i in range(8) :
    for j in range(8) :
        if graph[i][j] == INF :
            graph[i][j] = abs(dic[i][0] - dic[j][0]) + abs(dic[i][1] - dic[j][1])

# 6. 플루이드-워셜 알고리즘 수행
graph[0][7], graph[7][0] = abs((xe - xs)) + abs((ye - ys)), abs((xe - xs)) + abs((ye - ys))
for k in range(8) :
    for i in range(8) :
        for j in range(8) :
            if i!=j :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 7. 결과 출력
print(graph[0][7])