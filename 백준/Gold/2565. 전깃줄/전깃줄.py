import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
# 1. 전깃줄 정보 정렬
array = sorted([list(map(int, input().split())) for _ in range(n)])
# 2. LIS 리스트 선언
LIS = [array[0][1]]
# 3.
for _, b in array[1:] :
    # 3-1. 현재 LIS 내 최댓값보다 b 값이 더 클 경우
    if LIS[-1] < b :
        # LIS 리스트에 삽입
        LIS.append(b)
    # 3-2. 현재 LIS 내 최댓값이 b 값보다 더 클 경우
    else :
        idx = bisect_left(LIS, b)
        # LIS 업데이트
        LIS[idx] = b
# 4. 결과 출력
print(n - len(LIS))