def solution(arr):
    answer = [0, 0]
    n = len(arr)
    # 1. 재귀함수 선언
    def quad_tree(x, y, size) :
        # 2. 비교 수 설정
        stand = arr[x][y]
        # 3.
        for i in range(x, x+size) :
            for j in range(y, y+size) :
                # 4. 모두 같은 수로 이루어져 있는지 확인
                if arr[i][j] != stand :
                    # 5. 같은 수로 이루어지지 않은 경우
                    # 6. size 재조정
                    size //= 2
                    # 7. 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순으로 재귀함수 실행
                    quad_tree(x, y, size)
                    quad_tree(x, y+size, size)
                    quad_tree(x+size, y, size)
                    quad_tree(x+size, y+size, size)
                    return
        # 8. 같은 수로 이루어져 있는 경우 '개수 세기'
        answer[stand] += 1
        return 
    # 9. 재귀함수 실행
    quad_tree(0, 0, n)
    return answer