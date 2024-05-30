import sys
from heapq import heappush, heappushpop
input = sys.stdin.readline

n = int(input())
# 1. 강의 정보 리스트 생성 후 정렬
class_information = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : [x[1], x[2]])
# 2. 힙 리스트 생성
heap = []
# 3.
for _, start, end in class_information :
    # 3-1. 힙이 비었거나 힙의 최솟값이 현재 강의 시작 시간보다 클 경우
    if not heap or heap[0] > start : heappush(heap, end)
    # 3-2. 이외의 경우
    else : heappushpop(heap, end)
# 4. 결과 출력
print(len(heap))