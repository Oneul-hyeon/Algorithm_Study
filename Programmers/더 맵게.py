import heapq
def solution(scoville, K):
    answer = 0
    # 1. 해당 리스트 힙 정렬하기
    heapq.heapify(scoville)
    # 2. while문 - 조건 : 리스트 최소값이 k 이상일 때까지
    while scoville[0] < K :
        # 2-1. 힙에서 가장 작은 두 수 꺼내기
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        # 2-2. 주어진 식에 따라 처리
        # 2-3. 다시 힙에 push
        result = x + (y * 2)
        heapq.heappush(scoville, result)
        answer += 1
        # 4. 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1 return
        if len(scoville) == 1 :
            if scoville[0] < K : return -1
    # 3. while문이 돌아간 총 횟수 출력
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))