import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

text = input().rstrip()
# 1. state 변수 선언
state = False
count = 0
for i in range(len(text)) :
    # case 1 구현
    if i < len(text) - 1 :
        if state == False :
            if text[i].isupper() :
                # if 문에 속할 경우 마름모 버튼, 그냥 통과할 경우 별 버튼
                if text[i+1].isupper() :
                    state = True
                count += 1
        else :
            if text[i].islower() :
                # if 문에 속할 경우 마름모 버튼, 그냥 통과할 경우 별 버튼
                if text[i+1].islower() :
                    state = False
                count += 1
    # 3. case 2 구현
    else :
        # state 상태와 마지막 문자 상태가 다르면 카운트
        if state == False and text[-1].isupper() : count += 1
        elif state == True and text[-1].islower() : count += 1
# 4. 총 타이핑 횟수 출력(문자 길이 + count)
print(len(text) + count)