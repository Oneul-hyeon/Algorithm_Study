import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(input().rstrip().split())

# 1. +, - 만으로 갈 수 있는 최대 입력 횟수 구하기
min_count = abs(100 - n)
# 2. 1000000의 범위의 값들을 확인하며 최솟값 업데이트하기
for i in range(500000*2 + 1) :
    ch = str(i)
    for x in ch :
        if x in broken :
            break
    else :
        if min_count > abs(n - i) + len(ch) :
            min_count = abs(n - i) + len(ch)
print(min_count)