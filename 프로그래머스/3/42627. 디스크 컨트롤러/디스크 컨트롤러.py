from heapq import heappush, heappop
def solution(jobs):
    # 1. start, next 변수 생성
    answer = next = idx = 0
    start = -1
    heap = []
    # 2.
    while idx < len(jobs) :
        # 2-1.
        for s, t in jobs :
            # 현재 주어진 범위 내에 처리해야 할 작업이 있는 경우
            if start < s <= next :
                heappush(heap, (t, s))
        # 2-2. 힙이 값이 있는 경우
        if heap :
            # 값 추출
            job_t, job_s = heappop(heap)
            # start, next 재정의
            start = next
            next += job_t
            # 총 작업시간 업데이트
            answer += next - job_s
            idx += 1
        # 2-3. 힙에 값이 없는 경우
        else :
            # next 재정의
            next += 1
    # 3. 결과 리턴
    return answer // len(jobs)