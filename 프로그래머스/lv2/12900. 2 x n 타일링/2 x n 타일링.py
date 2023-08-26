def solution(n):
    # 1. dp 생성
    dp = [0] * (n+1)
    # 2. 초기값 설정
    dp[1], dp[2] = 1, 2
    # 3.
    for i in range(3, n+1) :
        # 점화식에 따라 처리
        dp[i] = (dp[i-1] + dp[i-2]) % 1_000_000_007
    # 4. 결과 리턴
    return dp[n]