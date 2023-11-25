import sys
input = sys.stdin.readline

# 1. 소수 판정 리스트 생성 함수 정의
def check_prime_number(num) :
    for i in range(2, int(num**0.5) + 1) :
        if num % i == 0 : return False
    return True

# 2. 제곱 수 생성 함수 정의
def power(a, p, mod) :
    if p == 1 : return a % mod
    x = power(a, p // 2, mod)
    if p % 2 == 0 : return (x * x) % mod
    else : return (x * x * a) % mod
def solution() :
    while True :
        p, a = map(int, input().split())
        # 종료 조건 설정
        if p == a == 0 : break
        # 소수 판별
        if not check_prime_number(p) and power(a, p, p) == a : print('yes')
        else : print('no')

if __name__ == "__main__" :
    solution()