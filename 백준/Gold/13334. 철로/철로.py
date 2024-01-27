import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n) :
    h, o = map(int, input().split())
    array.append((h, o) if h < o else (o, h))
d = int(input())

ans = 0
# 1. 리스트 정렬
array = sorted([info for info in array if info[1] - info[0] <= d], key = lambda x : x[1])
# 2. 힙 생성
heap = []
# 3.
for info in array :
    # 3-1. 힙에 값이 있을 경우
    if heap :
        # 3-1-1.
        while heap and heap[0][0] < info[1] - d:
            # 힙에서 값 제거
            heappop(heap)
    # 3-2. 힙에 값 추가
    heappush(heap, info)
    # 3-3. 최대 길이 업데이트
    ans = max(ans, len(heap))
# 4. 결과 출력
print(ans)