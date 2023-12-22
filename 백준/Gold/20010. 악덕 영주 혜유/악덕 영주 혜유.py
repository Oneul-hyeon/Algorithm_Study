import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(n, k, costs) :
    global max_distance
    # 1. Union 함수 정의
    def Union(x, y) :
        # 1-1. x, y의 루트 노드 찾기
        x = Find(x)
        y = Find(y)
        # 1-2. x > y 의 경우 루트 노드 정보 입력
        if x > y : roots[x] = y
        # 1-3. 이외의 경우 루트 노드 정보 입력
        else : roots[y] = x
    # 2. Find 함수 정의
    def Find(x) :
        # 2-1. 해당 노드가 루트 노드가 아닐 경우
        if x != roots[x] : return Find(roots[x])
        # 2-2. x 반환
        return x
    # 3. DFS 함수 정의
    def dfs(node, visited, dist) :
        global max_distance
        # 3-1. 최대 거리 업데이트
        if dist > max_distance :
            max_distance = dist
        # 3-2.
        for next, c in route[node] :
            # 방문하지 않았을 경우
            if not visited & (1 << next) :
                # dfs 실행
                dfs(next, visited | (1 << next), dist + c)

    # 4. 비용을 기준으로 오름차순 정렬
    costs.sort(key = lambda x : x[2])
    # 5. 루트 노드 리스트 생성
    roots = list(range(n+1))
    # 6.
    distance = 0
    route = defaultdict(list)
    for x, y, cost in costs :
        # 6-1. 사이클 테이블 확인
        if Find(x) != Find(y) :
            route[x].append((y, cost))
            route[y].append((x, cost))
            # 거리 추가
            distance += cost
            Union(x, y)
    # 7. dfs 실행
    for start in route.keys() :
        # 7-1. DFS 실행
        dfs(start, (1 << start), 0)
    # 8. 결과 출력
    print(distance)
    print(max_distance)
    
if __name__ == "__main__" :
    n, k = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(k)]
    max_distance = -int(1e9)
    solution(n, k, costs)