import sys
input = sys.stdin.readline

ans = int(1e9)
def solution(n, k, graph) :
    # 1. 모든 행성 탐사 시간 체크 함수 정의
    def check() :
        # 1-1. 출력 변수 정의
        time = 0
        # 1-2.
        for i in range(n-1) :
            # 행성 이동 시간 더하기
            a, b = route[i], route[i+1]
            time += graph[a][b]
        # 1-3. 결과 리턴
        return time
    # 2. 백트래킹 함수 정의
    def backtracking(cnt) :
        global ans
        # 2-1. 종료 조건 설정
        if cnt == n :
            # 최소 거리 업데이트
            ans = min(ans, check())
            return
        # 2-2.
        for i in range(n) :
            if visited[i] : continue
            # 2-2-1. 행성 경로 리스트에 행성 번호 삽입
            route.append(i)
            visited[i] = True
            # 2-2-2. 백트래킹 실행
            backtracking(cnt + 1)
            # 2-2-3. 행성 경로 리스트에 행성 번호 제거
            route.pop()
            visited[i] = False

    # 3. 플로이드-워셜을 통해 행성 간 최소 시간 재정의
    for z in range(n) :
        for a in range(n) :
            for b in range(n) :
                if a != b :
                    graph[a][b] = min(graph[a][b], graph[a][z] + graph[z][b])
    # 4. 행성 이동 경로 리스트 생성
    route = [k]
    visited = [False for _ in range(n)]
    visited[k] = True
    # 5. 백트래킹 실행
    backtracking(1)
    # 6. 결과 출력
    print(ans)

if __name__ == "__main__":
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    solution(n, k, graph)