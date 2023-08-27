from heapq import heappush, heappop
# 1. 최대 힙 리스트 생성 함수 선언
def max_heap(works) :
    # 1-1. 힙 리스트 생성
    heap = []
    # 1-2.
    for work in works :
        # 힙에 작업량을 음수로 삽입
        heappush(heap, -work)
    # 1-3. 힙 리턴
    return heap
def solution(n, works):
    # 2. 최대 힙 리스트 함수를 통해 힙 반환
    heap = max_heap(works)
    # 3.
    for _ in range(n) :
        # 힙에서 최댓값을 꺼내 1을 더한 값을 힙에 삽입
        max_ = heappop(heap)
        heappush(heap, max_ + 1) if max_ else heappush(heap, 0)
    # 4. 야근 피로도 리턴
    return sum([num ** 2 for num in heap])
    return answer