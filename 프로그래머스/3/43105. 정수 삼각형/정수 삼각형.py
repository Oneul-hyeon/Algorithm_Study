def solution(triangle):
    # 1.
    for i in range(1, len(triangle)) :
        for j in range(len(triangle[i])) :
            # i행의 0번 인덱스일 경우
            if j == 0 : triangle[i][j] += triangle[i-1][j]
            # i행의 i번 인덱스일 경우
            elif j == i : triangle[i][j] += triangle[i-1][j-1]
            # 이외의 경우
            else : triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    # 2. 결과 리턴
    return max(triangle[-1])