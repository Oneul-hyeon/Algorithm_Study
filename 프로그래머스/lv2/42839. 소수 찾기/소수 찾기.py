def solution(numbers):
    # 1. 백트래킹 함수 생성
    def backtracking(number, lst) :
        # 1-1. 종료 조건 설정
        if not lst : return
        # 1-2. 
        for i in range(len(lst)) :
            # 다음 수 만들기
            number += lst[i]
            # 소수 판별
            if array[int(number)] : answer.add(int(number))
            # 백트래킹 함수 실행
            backtracking(number, lst[:i] + lst[i+1:])
            # 숫자 되돌리기
            number = number[:-1]
    # 2. 에라토스테네스의 체를 통한 소수 판별 리스트 생성
    array = [True] * 10000000
    array[0], array[1] = False, False
    for i in range(2, 10000000 // 2 + 1) :
        if array[i] :
            for j in range(i*2, 10000000, i) :
                array[j] = False
    # 3. 결과 출력 변수 생성
    answer = set()
    # 4. 백트래킹 실행
    backtracking('', numbers)
    # 5. 결과출력
    return len(answer)