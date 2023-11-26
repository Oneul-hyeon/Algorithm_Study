def solution(A, B):
    answer = 0
    # 1. A팀, B팀의 수를 내림차순으로 정렬
    A.sort(reverse = True)
    B.sort(reverse = True)
    # 2.
    i = 0
    for num in A :
        # B팀의 수가 더 클 경우
        if num < B[i] :
            # 카운팅
            answer += 1
            # B팀 인덱스 업데이트
            i += 1
    # 3. 결과 리턴
    return answer