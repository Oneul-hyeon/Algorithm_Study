import sys
input = sys.stdin.readline

def solution(v, e, array) :
    # 1. union 함수 정의
    def union(x, y) :
        # 1-1. 루트 노드 찾기
        x, y = find(x), find(y)
        # 1-2. 더 작은 값을 가지는 노드로 정보 업데이트
        if x > y : roots[x] = y
        else : roots[y] = x
    # 2. find 함수 정의
    def find(x) :
        # 2-1. 루트 노드가 아닌 경우 재귀를 통해 루트 노드 반환
        if x != roots[x] : return find(roots[x])
        return roots[x]
    # 3. 비용을 오름차순으로 리스트 정렬
    array.sort(key = lambda x : x[2])
    # 4. 루트 노드 리스트 생성
    roots = list(range(v+1))
    cost = 0
    # 5.
    for a, b, c in array :
        # 5-1. 사이클이 형성되지 않는 경우
        if find(a) != find(b) :
            # 가중치 업데이트
            cost += c
            # 간선 연결
            union(a, b)
    # 6. 결과 출력
    print(cost)
if __name__ == "__main__":
    v, e = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(e)]
    solution(v, e, array)