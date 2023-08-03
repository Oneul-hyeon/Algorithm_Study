import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    string = input().rstrip()
    # 1. 비밀번호 문자열 생성
    l_password, r_password = deque(), deque()
    # 2.
    for s in string :
        # 2-1. < 의 경우
        if s == '<' :
            if l_password :
                r_password.appendleft(l_password.pop())
        # 2-2. > 의 경우
        elif s == '>' :
            if r_password :
                l_password.append(r_password.popleft())
        # 2-3. - 의 경우
        elif s == '-' :
            if l_password :
                l_password.pop()
        # 2-4. 문자가 입력된 경우
        else :
            l_password.append(s)
    # 3. 두 개의 큐 합치기
    l_password.extend(r_password)
    # 4. 결과 출력
    print(''.join(list(l_password)))