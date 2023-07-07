def solution(n, costs):
    def union(x, y) :
        x = find(x)
        y = find(y)
        
        # 더 작은 루트 노드에 합친다.
        if x < y : root[y] = x
        else : root[x] = y
        
    def find(x) :
        # 루트 노드를 찾을 때까지 재귀 호출
        if root[x] != x : return find(root[x])
        return x
    answer = 0
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key = lambda x : x[2])
    # 루트 노드 리스트 생성
    root = list(range(n+1))
    for start, end, cost in costs :
        # 사이클 테이블 확인
        if find(start) != find(end) :
            answer += cost
            union(start, end)
    return answer