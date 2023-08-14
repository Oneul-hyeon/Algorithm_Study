def solution(sequence, k):
    answer = []
    l = len(sequence)
    summation = 0
    # 1. right 설정
    right =  0
    # 2.
    for left in range(l) :
        # 2-1. 총 합이 k보다 작을 경우
        while right < l and summation < k :
            summation += sequence[right]
            right += 1
        # 2-2. 총 합이 k일 경우
        if summation == k :
            if not answer : answer = [left, right - 1]
            else :
                if right - 1 - left < answer[1] - answer[0] :
                    answer = [left, right - 1]
        # 2-3. 총 합에서 left 제외
        summation -= sequence[left]
    # 3. 결과 출력
    return answer