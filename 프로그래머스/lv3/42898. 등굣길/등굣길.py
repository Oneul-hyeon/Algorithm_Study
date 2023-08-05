def solution(m, n, puddles):
    answer = 0
    puddles = [[q, p] for p, q in puddles]
    # 1. dp 생성
    dp = [[0] * (m+1) for _ in range(n+1)]
    # 2. 초기값 설정
    # 행
    for j in range(1, m+1) :
        if [1, j] in puddles : break
        dp[1][j] = 1
    # 열
    for i in range(1, n+1) :
        if [i, 1] in puddles : break
        dp[i][1] = 1
    # 3.
    for i in range(2, n+1) :
        for j in range(2, m+1) :
            # 3-1. 물에 잠겼을 경우 예외 처리
            if [i, j] in puddles : continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[-1][-1] % 1000000007