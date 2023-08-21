from collections import deque
def solution(n, wires):
    # 1. bfs 함수 정의
    def bfs(now) :
        # 1-1. 큐에 현재 노드 삽입
        queue = deque([now])
        # 1-2. 현재 위치 방문 처리
        visited[now] = True
        # 1-3. 방문 노드 수 변수 생성
        count = 1
        # 1-4.
        while queue :
            # 노드 반환
            now = queue.popleft()
            for next in line[now] :
                # 다음 노드에 방문한 적이 없는 경우
                if not visited[next] :
                    # 방문 노드 수 업데이트
                    count += 1
                    # 방문 처리
                    visited[next] = True
                    # 큐에 다음 노드 추가
                    queue.append(next)
        # 1-5. 총 방문 노드 수 반환
        return count
    answer = int(1e9)
    # 2. 노드 별 간선 정보 리스트 생성
    line = [[] for _ in range(n+1)]
    for s, e in wires :
        line[s].append(e)
        line[e].append(s)
    # 3. 
    for s, e in wires :
        # 3-1. 방문 여부 리스트 생성
        visited = [False] * (n+1)
        # 3-2. 간선 제외
        line[s].remove(e)
        line[e].remove(s)
        now = []
        # 3-3.
        for i in range(1, n+1) :
            # 해당 위치에 방문한 적이 없을 경우 bfs실행
            if not visited[i] :
                now.append(bfs(i))
        # 3-4. 간선 복구
        line[s].append(e)
        line[e].append(s)
        # 3-5. 결과값 업데이트
        answer = min(answer, abs(now[0] - now[1]))
    # 4. 결과 리턴
    return answer