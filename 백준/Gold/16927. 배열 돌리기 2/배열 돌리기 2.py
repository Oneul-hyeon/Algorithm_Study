import sys
input = sys.stdin.readline

# 1. 재귀 함수 선언
def rotate(i, j, n, m) :
    # 3. 특정 위치 4개 값 별도 저장
    left_top = graph[i][j]
    left_bottom = graph[n-1][j]
    right_bottom = graph[n-1][m-1]
    right_top = graph[i][m-1]
    # 4. 위쪽 라인 돌리기
    for y in range(j, m-1) : graph[i][y] = graph[i][y+1]
    # 5. 왼쪽 라인 돌리기
    for x in range(n-1, i, -1) : graph[x][j] = graph[x-1][j]
    # 6. 아래쪽 라인 돌리기
    for y in range(m-1, j, -1) : graph[n-1][y] = graph[n-1][y-1]
    # 7. 오른쪽 라인 돌리기
    for x in range(i, n-1) : graph[x][m-1] = graph[x+1][m-1]
    # 8. 3에서 별도 저장한 값 넣어주기
    graph[i+1][j] = left_top
    graph[n-1][j+1] = left_bottom
    graph[n-2][m-1] = right_bottom
    graph[i][m-2] = right_top
    return

# 10. n, m, r 입력받기
N, M, R = map(int, input().split())
# 11. 배열 입력받기
graph = [list(map(int, input().split())) for _ in range(N)]
# 12. for문 <- 범위 : 얼마나 깊이 들어가야 하는지
for count in range(min(N, M)//2) :
    period = (N - 1 - 2*count) * 2 + (M - 1 - 2*count) * 2
    for _ in range(R%period) :
        rotate(count, count, N-count, M-count)
# 13. 결과 출력
for line in graph :
    print(*line)