from collections import deque
from itertools import islice
def solution(number, k):
    # 1. 스택 생성
    stack = deque([])
    # 2. 주어진 숫자를 숫자형 리스트로 변환
    number = deque(list(map(int, number)))
    # 3.
    while k != 0 and number:
        # 3-1. 스택이 비어있을 경우
        if not stack :
            stack.append(number.popleft()) # 스택에 다음 수 삽입
            continue
        # 3-2. 스택의 마지막 수가 다음 수보다 작을 경우
        if stack[-1] < number[0] :
            stack.pop()
            k -= 1
        # 3-3. 스택의 마지막 수가 다음 수보다 클 경우
        else :
            stack.append(number.popleft())
    
    return ''.join(map(str, islice(stack, 0, len(stack) - k ))) if k else ''.join(map(str, stack + number))