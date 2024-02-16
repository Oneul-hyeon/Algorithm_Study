import sys
input = sys.stdin.readline

S, T = input().rstrip(), input().rstrip()
# 1.
while len(T) != len(S) :
    # 1-1. 마지막 문자가 A인 경우
    if T[-1] == 'A' : T = T[:-1]
    # 1-2. 마지막 문자가 B인 경우
    else : T = T[:-1][::-1]
# 2. 결과 출력
print(1 if S == T else 0)