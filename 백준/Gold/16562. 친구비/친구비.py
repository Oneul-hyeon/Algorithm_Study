import sys
input = sys.stdin.readline

def solution(n, m, s, cost) :
    # 1. Union 함수 정의
    def union(x, y) :
        # 1-1. 두 노드의 루트 노드 찾기
        x = find(x)
        y = find(y)
        # 1-2. 더 작은 쪽에 업데이트
        if x > y : roots[x] = y
        else : roots[y] = x
    # 2. Find 함수 정의
    def find(x) :
        # 2-1. 주어진 수가 루트 노드가 아닌 경우
        if x != roots[x] :
            roots[x] = find(roots[x])
        return roots[x]
    roots = list(range(n+1))
    # 3.
    for _ in range(m) :
        x, y = map(int, input().split())
        # Union 함수 실행
        union(x, y)
    # 4.
    for x in range(1, n+1) :
        if roots[x] != find(x) :
            find(x)
    # 5.
    answer = 0
    for r in list(set(roots[1:])) :
        # 결과값 업데이트
        answer += min([cost[idx] for idx in range(1, n+1) if r == roots[idx]])
    # 6. 결과 출력
    print(answer if answer <= s else "Oh no")
    
if __name__ == "__main__" :
    n, m, s = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    solution(n, m, s, cost)