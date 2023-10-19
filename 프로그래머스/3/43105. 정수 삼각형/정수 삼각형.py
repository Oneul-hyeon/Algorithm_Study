def solution(triangle):
    # 1. dp 생성
    dp = [[0 for _ in range(i)] for i in range(1, len(triangle) + 1)]
    # 2. 초기값 설정
    dp[0][0] = triangle[0][0]
    # 3.
    for i in range(1, len(triangle)) :
        for j in range(len(triangle[i])) :
            # i행의 0번 인덱스일 경우
            if j == 0 : dp[i][j] = dp[i-1][j] + triangle[i][j]
            # i행의 i번 인덱스일 경우
            elif j == i : dp[i][j] = dp[i-1][j-1] + triangle[i][j] 
            # 이외의 경우
            else : dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    # 4. 결과 리턴
    return max(dp[-1])