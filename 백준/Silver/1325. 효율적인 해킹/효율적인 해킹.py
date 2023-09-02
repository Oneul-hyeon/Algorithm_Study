import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs(x) :
    # 1-4-1. 큐에 현재 위치 삽입
    queue = deque([x])
    # 1-2. 방문 여부 리스트 생성
    visited = [False] * (n+1)
    # 1-3. 현재 위치 방문 처리
    visited[x] = True
    cnt = 1
    # 1-4.
    while queue :
        # 1-4-1. 위치 인덱스 반환
        x = queue.popleft()
        # 1-4-2.
        for nx in relationship[x] :
            # 방문한 적이 없는 경우
            if not visited[nx] :
                # 방문 처리
                visited[nx] = True
                # 카운팅
                cnt += 1
                # 큐에 다음 위치 삽입
                queue.append(nx)
    # 1-5. 카운트 반환
    return cnt
n, m = map(int, input().split())
# 2. 신뢰 관계 리스트 생성
relationship = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    relationship[b].append(a)
# 3. 출력 리스트 생성
ans = []
max_ = -int(1e9)
# 4.
for i in range(1, n+1) :
    cnt = bfs(i)
    # 4-1. 최대 해킹 횟수와 같을 경우
    if cnt == max_ : ans.append(i)
    # 4-2. 최대 해킹 횟수보다 클 경우
    elif cnt > max_ :
        ans = [i]
        max_ = cnt
# 5. 결과 출력
print(*ans)