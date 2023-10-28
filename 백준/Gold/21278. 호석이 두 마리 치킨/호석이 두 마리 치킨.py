import sys
from itertools import combinations
input = sys.stdin.readline

def solution(n, m) :
    # 1. 플로이드-워셜을 위한 그래프 생성
    graph = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]
    # 2. 간선 정보 입력 받기
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    # 3. 플로이드-워셜
    for k in range(1, n+1) :
        for a in range(1, n+1) :
            for b in range(1, n+1) :
                if a != b :
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    # 4. 조합 리스트 생성
    combination = list(combinations(range(1, n+1), 2))
    # 5. 정렬
    combination.sort(key = lambda x : [sum([2 * min(graph[i][x[0]], graph[i][x[1]]) for i in range(1, n+1) if i not in x]), min(x), max(x)])
    n1, n2 = combination[0][0], combination[0][1]
    # 6. 결과 출력
    print(*combination[0], sum([2 * min(graph[i][n1], graph[i][n2]) for i in range(1, n+1) if i not in (n1, n2)]))

if __name__ == "__main__":
    n, m = map(int, input().split())
    solution(n, m)