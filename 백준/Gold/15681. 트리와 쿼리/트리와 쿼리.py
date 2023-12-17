import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
visited = 0
def solution(n, r, q):
    # 1. DFS 함수 생성
    def dfs(now) :
        global visited
        # 1-1. 방문 처리
        visited |= ( 1 << now )
        # 1-2.
        for next in graph[now] :
            # 1-2-1. 이미 방문했다면 continue
            if visited & (1 << next) : continue
            # 1-2-2. DFS 실행
            dfs(next)
            # 1-2-3. 점화식에 따라 값 추가
            dp[now] += dp[next]
    # 2. 간선 정보 입력받기
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 3. dp 생성
    dp = [1 for _ in range(n+1)]
    # 4. 방문 여부 변수 생성
    # 5. DFS 실행
    dfs(r)
    # 6. 결과 출력
    for _ in range(q) :
        print(dp[int(input())])

if __name__ == "__main__" :
    n, r, q = map(int, input().split())
    solution(n, r, q)