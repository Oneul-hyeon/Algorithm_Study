import sys
input = sys.stdin.readline

def solution(n, m, array) :
    # 1. union 함수 정의
    def union(x, y) :
        # 1-1. 루트 노드 찾기
        x, y = find(x), find(y)
        # 1-2. 더 작은 쪽에 합친다
        if x > y : root[x] = y
        else : root[y] = x
    # 2. find 함수 정의
    def find(x) :
        # 2-1. 루트 노드가 아니라면 찾을 때까지 함수 호출
        if x != root[x] : return find(root[x])
        return root[x]
    # 3. 각 컴퓨터 간 비용 리스트 정렬
    array.sort(key = lambda x : x[2])
    # 4. 루트 노드 리스트 생성
    root = list(range(n+1))
    cost = 0
    # 5.
    for x, y, c in array :
        # 5-1. 사이클이 형성되지 않는 경우
        if find(x) != find(y) :
            # 5-1-1. 비용 업데이트
            cost += c
            # 5-1-2. 간선 연결
            union(x, y)
    # 6. 결과 출력
    print(cost)

if __name__ == "__main__":
    n, m = int(input()), int(input())
    array = [list(map(int, input().split())) for _ in range(m)]
    solution(n, m, array)