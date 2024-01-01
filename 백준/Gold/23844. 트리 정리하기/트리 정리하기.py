import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solution(n, k) :
    # 1. 자식 노드의 수 추출 함수 설정
    def dfs(now, level) :
        global visited
        # 1-1. 방문 처리
        visited |= (1 << now)
        # 1-2.
        for next in graph[now] :
            # 1-2-1. 방문한 경우 continue
            if visited & (1 << next) : continue
            # 1-2-2. 현재 레벨의 노드 수가 k개 이하일 경우 카운팅
            if level_cnt[level] < k : level_cnt[level] += 1
            # 1-2-3. dFS 실행
            dfs(next, level + 1)

    # 2. 그래프 생성 후 간선 정보 입력
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    level_cnt = [0 for _ in range(n+1)]
    level_cnt[0] = 1
    # 3. dfs 실행
    dfs(1, 1)
    # 4. 결과값 출력
    print(sum(level_cnt))

if __name__ == "__main__" :
    n, k = map(int, input().split())
    visited = 0
    solution(n, k)