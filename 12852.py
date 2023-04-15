import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
# n == 1이라면 1까지 가는 연산은 0개
if n == 1 : print(f'{0}\n{1}')
else :
    # 초기값 설정
    dp[2] = 1
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + 1
        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2]+1)
    print(dp[n])

    x = dp[n]
    print(n, end =' ')
    while x != 0 :
        # print(dp[n-1], dp[n//3], dp[n//2], x-1)
        if n%3 == 0 and dp[n//3] == x-1 : n = n//3
        elif n%2 == 0 and dp[n//2] == x-1 : n = n//2
        elif dp[n - 1] == x - 1: n -= 1
        print(n, end = ' ')
        x -= 1



