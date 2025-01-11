def solution(triangle):
    # 1.
    for x, row in enumerate(triangle) :
        if x == 0 : continue
        for y, num in enumerate(row) :
            # 1-1. 가장 왼쪽의 경우
            if y == 0 :
                triangle[x][y] += triangle[x-1][y]
            # 1-2. 가장 오른쪽의 경우
            elif y == len(row)-1 :
                triangle[x][y] += triangle[x-1][y-1]
            # 1-3. 이외의 경우
            else :
                triangle[x][y] += max(triangle[x-1][y], triangle[x-1][y-1])
    # 2. 최댓값 return
    return max(triangle[-1])