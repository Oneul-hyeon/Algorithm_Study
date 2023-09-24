from heapq import heappush, heappop, heapify, nlargest

def solution(operations):
    # 1. 힙 리스트 생성
    heap = []
    # 2.
    for command in operations :
        # 2-1. 삽입 명령의 경우
        if command[0] == 'I' :
            # 최대, 최소 힙에 삽입
            num = int(command.split(' ')[1])
            heappush(heap, num)
        # 2-2. 삭제 명령일 경우
        else :
            # 힙이 비었을 경우 무시
            if not heap: continue
            # 최솟값 삭제 명령일 경우
            if command.split(' ')[1] == '-1':
                print(heap)
                heappop(heap)
            # 최댓값 삭제 명령일 경우
            else:
                heap = nlargest(len(heap), heap)[1:]
                heapify(heap)
    # 3. 결과 출력
    return [0, 0] if not heap else [nlargest(1, heap)[0], heap[0]]