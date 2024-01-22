import sys
input = sys.stdin.readline

# 1. DFS 함수 정의
def dfs(now, depth) :
    global visited

    # 1-1. 종료 조건 설정
    if depth == 5 :
        print(1)
        exit()
    # 1-2.
    for next in range(n) if now == -1 else graph[now] :
        # 1-2-1. 이미 처리된 경우 continue
        if visited & ( 1 << next ) : continue
        # 1-2-2. 방문 처리
        visited |= ( 1 << next )
        # 1-2-3. DFS 실행
        dfs(next, depth + 1)
        # 1-2-4. 방문 해제
        visited ^= ( 1 << next )

n, m = map(int, input().split())
# 2. 그래프 생성 후 친구 관계 입력
graph = [[] for _ in range(n)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = 0
# 3. DFS 실행 결과 출력
dfs(-1, 0)
# 4. 0 출력
print(0)