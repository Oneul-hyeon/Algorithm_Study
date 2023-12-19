import sys
input = sys.stdin.readline

def solution(n, m) :
    # 1. 벨만 포드 함수 정의
    def bf(start) :
        # 1-1. 시작 노드 초기화
        distance[start] = 0
        # 1-2.
        for i in range(n) :
            # 1-2-1.
            for j in range(m) :
                now, next, cost = edges[j]
                # 현재 간선을 거쳐 다음 노드로 가는 것이 더 빠를 경우
                if distance[now] != INF and distance[next] > distance[now] + cost :
                    distance[next] = distance[now] + cost
                    # 마지막에도 값이 변할 경우 False 반환
                    if i == n-1 : return False
        # 1-3. True 반환
        return True
    # 2. 간선 정보 입력
    edges = []
    for _ in range(m) :
        a, b, c = map(int ,input().split())
        edges.append((a, b, c))
    # 3.최단 거리 테이블 생성
    INF = float('inf')
    distance = [INF for _ in range(n+1)]
    # 4. 벨만 포드 실행
    state = bf(1)
    # 5. 결과 출력
    if not state : print("-1")
    else :
        for dist in distance[2:] :
            print(-1 if dist == INF else dist)

if __name__ == "__main__" :
    n, m = map(int, input().split())
    solution(n, m)