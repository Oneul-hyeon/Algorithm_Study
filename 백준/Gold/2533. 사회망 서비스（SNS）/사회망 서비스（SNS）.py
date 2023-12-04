import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(n):
    # 1. DFS 함수 정의
    def dfs(node) :
        # 1-1. 방문 처리
        visited[node] = True
        # 1-2.
        for nn in graph[node] :
            # 1-2-1. 방문한 적이 있는 경우
            if visited[nn] : continue
            # 1-2-2. DFS 실행
            dfs(nn)
            # 1-2-3. 해당 노드가 얼리어답터일 경우
            dp[node][1] += min(dp[nn])
            # 1-2-4. 해당 노드가 얼리어답터가 아닐 경우
            dp[node][0] += dp[nn][1]

    # 2. DP 생성
    dp = [[0, 1] for _ in range(n+1)]
    # 3. 간선 정보 리스트 생성 후 정보 입력
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1) :
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # 4. 방문 여부 리스트 생성
    visited = [False for _ in range(n+1)]
    # 5. DFS 실행
    dfs(1)
    # 6. 결과 출력
    print(min(dp[1]))

if __name__ == "__main__" :
    n = int(input())
    solution(n)