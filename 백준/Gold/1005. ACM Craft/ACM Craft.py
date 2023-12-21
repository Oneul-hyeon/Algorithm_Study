import sys
from collections import deque
input = sys.stdin.readline

def solution(t) :
    for _ in range(t) :
        n, k = map(int, input().split())
        costs = [0] + list(map(int, input().split()))
        # 1. 모든 노드의 진입차수 리스트 생성
        indegree = [0 for _ in range(n+1)]
        # 2. 그래프 생성 후 간선 정보 입력 받기
        graph = [[] for _ in range(n+1)]
        for _ in range(k) :
            x, y = map(int, input().split())
            graph[x].append(y)
            # 2-1. 진입 차수 카운팅
            indegree[y] += 1
        # 3. DP 생성
        dp = [-float('inf') for _ in range(n+1)]
        # 4. 큐를 생성해 진입 차수가 0인 노드를 큐에 삽입
        queue = deque()
        for i in range(1, n+1) :
            if indegree[i] == 0 :
                queue.append(i)
                # 4-1. DP 초기값 설정
                dp[i] = costs[i]
        # 5.
        while queue :
            # 5-1. 큐에서 원소 꺼내기
            now = queue.popleft()
            # 5-2.
            for next in graph[now] :
                # 5-2-1. 점화식에 따라 DP 값 변경
                dp[next] = max(dp[next], dp[now] + costs[next])
                # 5-2-2. 진입 차수 감소
                indegree[next] -= 1
                # 5-2-3. 진입 차수가 0일 경우 큐에 삽입
                if indegree[next] == 0 :
                    queue.append(next)
        # 6. 결과 출력
        target = int(input())
        print(dp[target])
        
if __name__ == "__main__" :
    t = int(input())
    solution(t)