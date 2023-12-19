import sys
input = sys.stdin.readline

# 1. 블록 이동 함수 정의
def move_block(n, now_graph, dir) :
    new_graph = [now[:] for now in now_graph]
    # 1-1. 오른쪽으로 이동하는 경우 행렬 변경
    if dir == 1 :
        new_graph = [new[::-1] for new in new_graph]
    # 1-2. 아래쪽으로 이동하는 경우 행렬 변경
    elif dir == 2 :
        new_graph = [list(new)[::-1] for new in zip(*new_graph)]
    # 1-3. 위쪽으로 이동하는 경우 행렬 변경
    elif dir == 3 :
        new_graph = [list(new) for new in zip(*new_graph)]
    for i, line in enumerate(new_graph) :
        new_graph[i] = [num for num in line if num]
    # 1-4.
    for i, row in enumerate(new_graph) :
        idx = 0
        new_row = []
        while idx < len(row) :
            if idx == len(row) - 1 or row[idx] != row[idx + 1] :
                new_row.append(row[idx])
                idx += 1
            else :
                new_row.append(2 * row[idx])
                idx += 2
        new_graph[i] = new_row + [0 for _ in range(n - len(new_row))]
    # 1-5. 오른쪽으로 이동하는 경우 행렬 원위치
    if dir == 1 :
        new_graph = [new[::-1] for new in new_graph]
    # 1-6. 아래쪽으로 이동하는 경우 행렬 원위치
    elif dir == 2 :
        new_graph = [list(line) for line in zip(*[new[::-1] for new in new_graph])]
    # 1-7. 위쪽으로 이동하는 경우 행렬 원위치
    elif dir == 3 :
        new_graph = [list(new) for new in zip(*new_graph)]
    return new_graph
# 2. 백트래킹 함수 정의
def backtracking(cnt, now_graph) :
    global ans
    # 2-1. 종료 조건 설정
    if cnt == m :
        # 가장 큰 블록의 값 업데이트
        ans = max(ans, max([max(line) for line in now_graph]))
        return
    # 2-2.
    for dir in range(4) :
        # 백트래킹 함수 실행
        backtracking(cnt+1, move_block(n, now_graph, dir))
def solution(n, graph) :
    global ans
    # 4. 백트래킹 실행
    backtracking(0, graph)
    # 5. 결과 출력
    print(ans)

if __name__ == "__main__" :
    n = int(input())
    m = 5
    graph = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    solution(n, graph)