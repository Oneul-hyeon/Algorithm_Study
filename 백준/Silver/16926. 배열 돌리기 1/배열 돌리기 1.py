import sys
input = sys.stdin.readline

# 1. 재귀함수 선언
def rotate(start) :
    # 1-1. 기존의 모서리값 저장
    left_top = array[start][start]
    right_top = array[start][m-1-start]
    left_bottom = array[n-1-start][start]
    right_bottom = array[n-1-start][m-1-start]
    # 1-2. 윗부분 배열 돌리기
    for i in range(start+1, m-start):
        array[start][i-1] = array[start][i]
    # 1-3. 왼쪽부분 배열 돌리기
    for i in range(n-start-1, start, -1) :
        array[i][start] = array[i-1][start]
    # 1-4. 아랫부분 배열 돌리기
    for i in range(m-1-start, start, -1):
        array[n-1-start][i] = array[n-1-start][i-1]
    # 1-5. 오른쪽부분 배열 돌리기
    for i in range(start+1,n-start) :
        array[i-1][m-1-start] = array[i][m-1-start]

    # 1-6. 값 변경이 필요한 위치에 기존의 각 모서리 값 대입
    array[start+1][start] = left_top
    array[start][m-start-2] = right_top
    array[n-1-start][start+1] = left_bottom
    array[n-2-start][m-1-start] = right_bottom

n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r) :
    # 2. n, m 중 작은 수//2만큼 배열 돌리기
    x = min(n, m)
    for i in range(x//2):
        rotate(i)
for line in array :
    print(*line)


    