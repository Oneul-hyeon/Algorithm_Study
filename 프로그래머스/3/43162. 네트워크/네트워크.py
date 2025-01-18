from collections import deque

def solution(n, computers):
    # 1. BFS 함수 정의
    def bfs(node) :
        nonlocal visited
        
        # 1-1. 큐 생성 후 노드 번호 삽입
        queue = deque([])
        queue.append(node)
        # 1-2. 현재 노드 방문 처리
        visited |= (1 << node)
        # 1-3.
        while queue :
            # 1-3-1. 큐에서 노드 반환
            now = queue.popleft()
            # 1-3-2.
            for next, connected in enumerate(computers[now]) :
                # 연결된 노드에 방문한 적이 없는 경우
                if connected and not visited & (1 << next) :
                    # 방문 처리
                    visited |= (1 << next)
                    # 큐에 다음 노드 삽입
                    queue.append(next)
    ans = 0
    # 2. 방문 여부 변수 생성
    visited = 0
    # 3.
    for idx in range(n) :
        # 3-1. 해당 노드에 방문한 적이 없는 경우
        if not visited & (1 << idx) :
            # 3-1-1. BFS 수행
            bfs(idx)
            # 3-1-2. 네트워크 카운트
            ans += 1
    # 4. 총 네트워크 갯수 반환
    return ans