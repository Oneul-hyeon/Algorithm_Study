import sys
from collections import deque
input = sys.stdin.readline

# 1. dfs 함수 정의
def dfs(destination) :
    global ans_dfs
    # 1-1. 종료 조건 설정
    if not graph[destination] or False not in visited_dfs[1:]: return
    # 1-2. for문
    for node in graph[destination] :
        if not visited_dfs[node] :
            visited_dfs[node] = True
            ans_dfs.append(node)
            dfs(node)

# 2. bfs 함수 정의
def bfs(destination) :
    global ans_bfs

    queue = deque()
    # 2-1. 큐에 현재 위치 삽입
    queue.append(destination)
    # 2-2. 방문 처리
    visited_bfs[destination] = True
    # 2-3.
    while queue :
        idx = queue.popleft()
        # 2-4.
        for node in graph[idx] :
            # 방문하지 않은 경우
            if not visited_bfs[node] :
                visited_bfs[node] = True
                ans_bfs.append(node)
                queue.append(node)
                
n, m, v = map(int, input().split())
# 3. 간선의 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in range(1, n+1) : graph[i] = sorted(graph[i])

# 4. 방문 여부 변수 설정
visited_dfs, visited_bfs = [False for _ in range(n+1)], [False for _ in range(n+1)]

# 5. DFS 실행
ans_dfs = [v]
visited_dfs[v] = True
dfs(v)
# 6. BFS 실행
ans_bfs = [v]
bfs(v)

print(*ans_dfs)
print(*ans_bfs)
