import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# 1. N, K 입력받기
n, k = map(int, input().split())
count = 0
# 2. while문
# 2-1. 2진수로 표현했을 때 1의 개수가 k가 될 때까지 n에 1 더해주기
while bin(n)[2:].count('1') > k :
    n += 1
    count += 1
# 3. 추가로 필요한 물통의 개수 출력
print(count)








