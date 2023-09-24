from heapq import heappush, heappop
from collections import defaultdict


def solution(operations):
    # 1. 최소힙, 최대힙 선언
    min_heap, max_heap = [], []
    # 2. 최대힙 딕셔너리, 최소힙 딕셔너리 선언
    max_dict, min_dict = defaultdict(int), defaultdict(int)
    # 3.
    for command in operations :
        # 3-1. 삽입 명령일 경우
        c1, c2 = command.split(' ')
        if c1 == 'I' :
            num = int(c2)
            # 최대, 최소힙에 삽입
            heappush(max_heap, -num)
            heappush(min_heap, num)
            # 각 딕셔너리에 카운트
            max_dict[num] += 1
            min_dict[num] += 1
        # 3-2. 삭제 명령일 경우
        else :
            # 힙이 비었을 경우 무시
            if not max_heap or not min_heap :
                if max_heap or min_heap :
                    min_heap, max_heap = [], []
                    max_dict, min_dict = defaultdict(int), defaultdict(int)
                continue
            # 최솟값 삭제 명령일 경우
            if c2 == '-1' :
                while min_heap :
                    num = heappop(min_heap)
                    # 최소 힙 딕셔너리에 해당 최솟값 1 감소
                    if min_dict[num] > 0 : min_dict[num] -= 1
                    # 최소 힙에서 추출한 최솟값이 최대힙에 있는 경우
                    if min_dict[num] < max_dict[num] : break
            # 최댓값 삭제 명령일 경우
            else :
                while max_heap :
                    num = -heappop(max_heap)
                    # 최소 힙 딕셔너리에 해당 최솟값 1 감소
                    if max_dict[num] > 0 : max_dict[num] -= 1
                    # 최소 힙에서 추출한 최솟값이 최대힙에 있는 경우
                    if min_dict[num] > max_dict[num] : break
                    
    # 4. 최소, 최대 힙 병합
    last_heap = set(min_heap) & set(list(map(lambda x : -x, max_heap)))
    # 5. 결과 출력
    return [0, 0] if not last_heap else [max(last_heap), min(last_heap)]