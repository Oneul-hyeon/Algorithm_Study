import sys
from collections import deque
input = sys.stdin.readline

# 5, bfs 함수 정의
def bfs(node) :
    # 5-1. 큐에 현재 노드 삽입
    queue = deque([node])
    # 5-2. 현재 위치 방문 처리
    visited[node] = True
    # 5-3.
    while queue :
        # 큐에서 위치 인덱스 반환
        node = queue.popleft()
        # 반환된 위치 인덱스와 연결된 노드 확인
        for x in nodes[node] :
            # 방문하지 않은 경우
            if not visited[x] :
                # 방문 처리
                visited[x] = True
                # 큐에 다음 위치 삽입
                queue.append((x))
    return 1
n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
ans = 0
# 1. 각 노드에 간선 정보 입력하기
for _ in range(m) :
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
# 2. 방문 여부 설정
visited = [False] * (n+1)
# 3. 이중 for문
for i in range(1, n+1) :
    if not visited[i] :
        ans += bfs(i)
# 6. 결과 출력
print(ans)