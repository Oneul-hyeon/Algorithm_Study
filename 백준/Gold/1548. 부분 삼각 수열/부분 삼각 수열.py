import sys
input = sys.stdin.readline

n = int(input())
max_len = -int(1e9)
# 1. 수열 정렬하기
array = sorted(list(map(int, input().split())))
# 2.
if n < 3 : max_len = n
else :
    for x in range(n-2) :
        # 3.
        for z in range(n-1, -1, -1) :
            # 4. 건너뛰는 조건
            if x + 1 > z : continue
            # 5. x+y > z 인 경우 최대 길이 업데이트
            if array[x] + array[x+1] > array[z] :
                max_len = max(max_len, z - x + 1)
print(max_len)