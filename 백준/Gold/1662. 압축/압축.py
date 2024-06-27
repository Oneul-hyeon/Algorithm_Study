import sys
input = sys.stdin.readline

array = list(input().strip())
# 1. 스택 생성
stack = []
# 2.
length, multiple = 0, 0
for s in array :
    # 2-1. 입력받은 문자가 "("일 경우
    if s == "(" :
        # 2-1-1. 스택에 값 삽입
        stack.append((length - 1, multiple))
        length = 0
    # 2-2. 입력받은 문자가 ")"일 경우
    elif s == ")" :
        # 2-2-1. 스택에서 값 제거
        length_, multiple_ = stack.pop()
        # 2-2-2. 현재 길이 업데이트
        length = length * multiple_ + length_
    else :
        length += 1
        multiple = int(s)
# 3. 결과 출력
print(length)