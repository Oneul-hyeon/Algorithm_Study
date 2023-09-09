import sys
input = sys.stdin.readline

string = input().rstrip()
l = len(string)

# 1. 문자열이 한 문자로만 구성되어 있는 경우
if len(set(string)) == 1 : print(-1)
# 2. 나머지 경우가 팰린드롬일 경우
elif string == string[::-1] : print(l - 1)
# 3. 원래 문자열이 팰린드롬이 아닐 경우
else : print(l)