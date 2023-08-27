def solution(n, money):
    # 1.dp 생성
    dp = [0] * (n+1)
    # 2. 초기값 설정
    dp[0] = 1
    # 3.
    for m in money :
        for i in range(m, n+1) :
            # 3-1. 현재 인덱스 - 현재 돈 인덱스에 값이 있는 경우
            if dp[i - m] :
                # 점화식에 따라 처리
                dp[i] += dp[i - m]
    # 4. 결과 리턴    
    return dp[n] % 1_000_000_007