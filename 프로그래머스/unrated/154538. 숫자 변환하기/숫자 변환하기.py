from collections import deque
def solution(x, y, n):
    if x == y : return 0
    # 1. 방문 여부 리스트 생성
    visited = [False] * (y+1)
    # 2. 큐에 (현재 위치, 0) 삽입
    queue = deque()
    queue.append((x, 0))
    # 3. 현재 위치 방문 처리
    visited[x] = True
    # 4. 
    while queue :
        # 4-1. 위치, 연산 횟수 반환
        x, count = queue.popleft()
        # 4-2.
        for nx in [x+n, 2*x, 3*x] :
            # 4-2-1. 예외처리
            if nx > y : continue
            # 4-2-2. 방문하지 않은 경우
            if not visited[nx] :
                # y 값에 도달할 경우
                if nx == y : return count + 1 # 연산횟수 + 1 반환
                else :
                    # 방문 처리
                    visited[nx] = True
                    # 큐에 (다음 위치, 연산 횟수 + 1) 삽입
                    queue.append((nx, count + 1))
    # 5. -1 반환
    return -1