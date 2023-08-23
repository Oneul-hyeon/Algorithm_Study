import heapq
def solution(book_time):
    # 1. 힙 리스트 생성
    heap = []
    # 2. book_time 정렬
    # 3.
    for start, end in sorted(book_time) :
        start = list(map(int, start.split(':')))
        end = list(map(int, end.split(':')))
        # 3-1. 힙 리스트에 값이 있으면서 대실 종료 시간 + 청소 시간의 최솟값이 다음 대실 시작 시간보다 작거나 같을 경우
        if heap and (start[0] > heap[0][0] or (start[0] == heap[0][0] and start[1] >= heap[0][1])) :
            # 힙에서 제거
            heapq.heappop(heap)
        # 3-2. 다음 대실 종료 시간 + 청소 시간 삽입
        heapq.heappush(heap,(end[0], end[1] + 10)) if end[1] + 10 < 60 else heapq.heappush(heap,(end[0]+1, (end[1]+10)%60))
    # 4. 힙 리스트 길이 출력
    return len(heap)