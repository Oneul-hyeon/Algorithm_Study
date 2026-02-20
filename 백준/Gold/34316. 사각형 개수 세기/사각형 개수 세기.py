import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 1. N이 더 큰 경우
if N>M:
    # 1-1. N, M 변경
    N, M = M, N
    # 1-2. 행, 열 변경
    graph = [row for row in zip(*graph)]
# 2.
for i in range(N-1):
    for j in range(i+1, N):
        # 2-1. 행 추출
        row_i, row_j = graph[i], graph[j]
        # 2-2. 열 별 덧셈값 리스트 생성
        summation = [0 for _ in range(19)]
        # 2-3.
        for x in range(M):
            # 2-3-1. 열 별 덧셈값 카운팅
            summation[row_i[x]+row_j[x]] += 1
        # 2-4.
        for x in range(2, 10):
            # 2-4-1. 합이 20이 되는 경우의 수 카운팅
            ans += summation[x] * summation[20-x]
        # 2-5. 합이 10이 되는 경우의 수 카운팅
        ans += summation[10] * (summation[10]-1) // 2
# 3. 결과 출력
print(ans)