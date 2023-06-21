import sys
input = sys.stdin.readline

def check(num) :
    # 1. 소수 여부 판별
    for i in range(2, int(num**0.5)+1) :
        if num % i == 0 : return False
    # 2. 팰린드롬 여부 판별
    return True if str(num) == str(num)[::-1] else False

n = int(input())
if n == 1 : n += 1
while True :
    if check(n) :
        print(n)
        break
    n += 1



