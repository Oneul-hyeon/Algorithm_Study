import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. (n+1) by (n+1) 행렬 만들기
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 2. 자기 자신과 자기 자신을 비교하는 부분 0으로 설정
for i in range(1, n+1) :
    graph[i][i] = 0

# 3. 친구 관계를 하나씩 입력
for _ in range(m) :
    a, b = map(int, input().split())
    # 3-1. 서로 친구관계이므로 양방향
    graph[a][b], graph[b][a] = 1, 1

# 4. 플루이드 워셜 알고리즘 수행
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = [0] * (n+1)
for i in range(1, n+1) :
    ans[i] = sum(graph[i][1:])
print(ans.index(min(ans[1:])))

