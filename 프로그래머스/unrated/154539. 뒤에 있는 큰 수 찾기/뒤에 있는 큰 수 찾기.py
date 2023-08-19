def solution(numbers):
    answer = []
    # 1. 리스트 뒤집기
    numbers = numbers[::-1]
    # 2. 스택 생성
    stack = []
    # 3.
    for num in numbers :
        # 3-1.
        while True :
            # 3-1-1. 스택이 비어있을 경우
            if not stack :
                # 출력 리스트에 -1 삽입
                answer.append(-1)
                # 스택에 현재 수 삽입
                stack.append(num)
                break
            # 3-1-2. 스택의 마지막 값이 현재 값보다 클 경우
            elif stack[-1] > num :
                # 출력 리스트에 스택의 마지막 값 삽입
                answer.append(stack[-1])
                # 스택에 현재 수 삽입
                stack.append(num)
                break
            # 3-1-3. 스택의 마지막 값이 현재 값보다 같거나 작을 경우
            else :
                stack.pop()
    return answer[::-1]