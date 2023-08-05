def solution(storey):
    answer = 0
    # 1. 총 정보를 리스트로 만들어 뒤집기
    storey = list(map(int, str(storey)))[::-1]
    length = len(storey)
    # 2. for 문
    for idx, num in enumerate(storey) :
        # 2-1. 마지막 인덱스의 경우
        if idx == length - 1 : answer += (10 - num) + 1 if num >= 6 else num
        # 2-2. 이외의 경우
        else :
            if num >= 6 or (num == 5 and storey[idx+1] >= 5) :
                answer += 10 - num
                storey[idx+1] += 1
            else :
                answer += num
    # 3. 결과 리턴
    return answer