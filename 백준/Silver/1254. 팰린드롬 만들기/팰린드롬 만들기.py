import sys
input = sys.stdin.readline

string1 = input().rstrip()
# 1. 뒤집힌 문자열 생성
string2 = string1[::-1]
l = 0
# 2.
while True :
    # 2-1. 추가 문자 생성
    plus_s = string1[:l]
    # 2-2. 팰린드롬 여부 확인
    if string1 + plus_s[::-1] == plus_s + string2 :
        # 팰린드롬일 경우 길이 출력
        print(len(string1) + l)
        break
    else : l+=1