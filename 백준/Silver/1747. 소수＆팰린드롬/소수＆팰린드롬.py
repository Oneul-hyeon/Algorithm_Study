import sys
input = sys.stdin.readline

# 4. check 재귀 함수 선언
def check(num) :
    # 4-1. 소수 여부 판별
    for i in range(2, int(num**0.5)+1) :
        if num % i == 0 : return False
    # 4-2. 팰린드롬 여부 판별
    return True if str(num) == str(num)[::-1] else False

n = int(input())
# 1. n=1일 경우 처리
if n == 1 : n += 1
# 2.
while True :
    # 3. check 재귀함수 실행
    if check(n) :
        print(n)
        break
    n += 1
