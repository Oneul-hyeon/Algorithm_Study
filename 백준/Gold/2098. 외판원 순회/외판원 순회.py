import sys
input = sys.stdin.readline

def solution(n, costs) :
    # 1. 최소 비용 추출 함수 정의
    def extraction(now, visited) :
        # 1-1. 이미 방문한 경로인 경우
        if dp[now][visited] : return dp[now][visited]
        # 1-2. 모든 도시를 방문한 경우
        if visited == (1 << n) - 1 :
            # 1-2-1. 마지막 도시에서 처음 도시로 가는 방법이 없는 경우
            if not costs[now][0] : return INF
            # 1-2-2. 이외의 경우
            return costs[now][0]
        # 1-3.
        min_cost = INF
        for next in range(1, n) :
            # 1-3-1. 다음 방향으로 갈 수 없거나 이미 방문한 도시인 경우
            if not costs[now][next] or visited & (1 << next) : continue
            # 1-3-2. 이외의 경우
            # 비용 구하기
            cost = costs[now][next] + extraction(next, (1 << next) | visited)
            # 1-3-3. 최소 비용 구하기
            min_cost = min(min_cost, cost)
        # 1-4. 최소 비용 업데이트
        dp[now][visited] = min_cost
        # 1-5. 결과 리턴
        return min_cost
    INF = float("inf")
    # 2. dp 생성
    dp = [[0 for _ in range(1 << n)] for _ in range(n)]
    # 3. 결과 출력
    print(extraction(0, 1))

if __name__ == "__main__" :
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    solution(n, costs)