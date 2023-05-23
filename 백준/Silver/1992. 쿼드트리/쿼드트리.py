import sys
input = sys.stdin.readline

# 3. 쿼드트리 재귀함수 생성
def quad_tree(x, y, size) :
    # 4. 비교값 설정
    stand = graph[x][y]
    # 5. 특정 구역이 1개의 수로만 이루어져 있는지 확인
    for i in range(x, x+size) :
        for j in range(y, y+size) :
            if graph[i][j] != stand :
                break
        else :
            continue
        break
    # 6. 특정 구역이 1개의 수로만 이루어져 있을 경우 1개의 수 출력
    else :
        print(stand,end='')
        return
    # 7. 특정 구역이 1개의 수로 이루어지지 않은 경우 다음 쿼드트리 실행
    size = size // 2
    print('(', end='')
    quad_tree(x, y, size)
    quad_tree(x, y+size, size)
    quad_tree(x+size, y, size)
    quad_tree(x+size, y+size, size)
    print(')',end='')

n = int(input())
# 1. 영상의 각 점들 입력받기
graph = [list(input().rstrip()) for _ in range(n)]
# 2. 쿼드트리 재귀함수 실행
quad_tree(0, 0, n)