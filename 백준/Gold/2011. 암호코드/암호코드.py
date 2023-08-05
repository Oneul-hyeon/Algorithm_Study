import sys
input = sys.stdin.readline

code = [0] + list(map(str, input().rstrip()))
n = len(code)
# 1. 맨 앞에 0 이 나오는 경우 0 출력
if code[1] == '0' : print(0)
else :
    # 2. dp 생성
    dp = [0] * n
    # 3. 초기값 설정
    dp[0] = dp[1] = 1
    # 4.
    for i in range(2, n) :
        # 4-1. 해당 수가 0보다 큰 경우
        if int(code[i]) > 0 : dp[i] += dp[i-1]
        # 4-2. 직전의 수를 붙였을 때 10 이상 26 이하인 경우
        if 10 <= int(''.join(code[i-1:i+1])) <= 26 : dp[i] += dp[i-2]
    # 5. 결과 출력
    print(dp[-1] % 1000000)