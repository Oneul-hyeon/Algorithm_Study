import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
boxs = list(map(int, input().split()))

# 1. 리스트 생성
array = [boxs[0]]
# 2.
for box in boxs[1:] :
    # 2-1. 현재 상자 크기가 리스크의 마지막 값보다 클 경우
    if array[-1] < box :
        array.append(box)
    # 2-2. 현재 상자 크기가 리스트의 마지막 값보다 작을 경우
    else :
        # 현재 상자 크기에 맞는 인덱스 구하기
        idx = bisect_left(array, box)
        # 해당 인덱스에 현재 상자 크기 입력
        array[idx] = box
# 3. 리스트 길이 출력
print(len(array))