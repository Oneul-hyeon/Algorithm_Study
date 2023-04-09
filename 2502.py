import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

d, k = map(int, input().split())
dp = [[0,0] for _ in range(31)]
dp[3] = [1,1]
dp[4] = [1,2]
# 1. dp를 이용해 할머니가 넘어온 날 d에 a와 b의 계수 구하기
for i in range(5, d+1) :
    dp[i] = [dp[i-1][0]+ dp[i-2][0], dp[i-1][1]+ dp[i-2][1]]

coef_a, coef_b = dp[d][0], dp[d][1]
# 2. d 날에 호랑이에게 준떡으로부터 가능한 b의 최댓값 구하기
max_b = k//coef_b
# 3. for 문을 활용
# 3-1. max_b(k//b의 계수)의 범위로 range 설정
for i in range(1, max_b+1) :
    mod = k - coef_b*i
    # 3-2. a가 맞아떨어지는지 확인
    if mod % coef_a == 0 :
        a = mod // coef_a
        b = i
        if a<= b :
            # 3-3. 결과 출력
            print(f'{a}\n{b}')


