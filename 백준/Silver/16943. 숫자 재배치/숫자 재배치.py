import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(number, lst) :
    global ans
    # 1-1. 종료 조건 설정
    if not lst :
        c = int(''.join(number))
        if c < b :
            ans = max(ans, c)
            print(ans)
            sys.exit()
    # 1-2.
    for i in range(len(lst)) :
        # 첫 글자가 0인 경우 continue
        if not number and lst[i] == '0' : continue
        # 백트래킹 함수 실행
        backtracking(number + [lst[i]], lst[:i] + lst[i+1:])

a, b = map(int, input().split())
array = sorted(list(str(a)), reverse = True)
length = len(array)
str_b = str(b)
ans = -1
# 2. 백트래킹 함수 실행
backtracking([], array)
# 3. 결과 출력
print(ans)