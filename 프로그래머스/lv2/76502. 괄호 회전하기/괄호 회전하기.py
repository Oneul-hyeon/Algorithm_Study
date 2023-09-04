def solution(s):
    # 1. 올바른 괄호 문자열 체크 함수 정의
    def check(s) :
        # 1-1. 스택 생성
        stack = []
        # 1-2.
        while s :
            # 1-2-1. 스택이 비었을 경우
            if not stack : stack.append(s.pop(0)) # 첫 값 삽입
            # 1-2-2. 스택이 비어있지 않을 경우
            else :
                # 스택의 마지막 문자와 남은 문자열의 앞 문자가 한 쌍일 경우
                if [stack[-1], s[0]] in [['[', ']'], ['{', '}'], ['(', ')']] :
                    stack.pop()
                    s.pop(0)
                # 이외의 경우
                else :
                    stack.append(s.pop(0))
        # 1-3. 결과 출력
        return 1 if not stack else 0
    answer = 0
    s = list(s)
    for x in range(len(s)) :
        # 문자 회전
        s.append(s.pop(0))
        # 체크 함수 실행
        answer += check(s.copy())
    return answer