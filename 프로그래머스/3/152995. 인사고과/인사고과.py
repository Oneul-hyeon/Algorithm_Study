def solution(scores):
    # 1. 원호의 점수 합 구하기
    wanho = scores[0]
    wanho_summation = sum(scores[0])
    # 2. 점수 목록 정렬
    scores.sort(key = lambda x : [-x[0], x[1]])
    # 3. 동료 평가 점수의 최댓값 변수 선언
    max_score = 0
    # 4.
    answer = 1
    for s1, s2 in scores :
        # 4-1. 완호의 점수가 해당 점수보다 낮을 경우 -1 리턴
        if wanho[0] < s1 and wanho[1] < s2 : return -1
        # 4-2. 동료 평가 점수가 현재 최댓값보다 낮은 경우
        if max_score <= s2 :
            # 4-2-1. 최댓값 업데이트
            max_score = s2
            # 4-2-2. 점수의 합이 완호보다 높은 경우 카운팅
            if s1 + s2 > wanho_summation : answer += 1
    # 5. 결과 리턴
    return answer