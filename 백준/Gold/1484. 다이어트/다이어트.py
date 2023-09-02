import sys, math
input = sys.stdin.readline

g = int(input())
ans = []
# 1. 기억하고 있는 몸무게 설정
remember = 1
# 2.
while True :
    # 2-1. 식이 맞아 떨어지는 경우 출력 리스트에 값 삽입
    calculation = math.sqrt(g + remember**2)
    if int(calculation) == calculation : ans.append(int(calculation))
    # 2-2. 현재 몸무게 값보다 기억하는 몸무게 값이 더 커지는 경우 탈출
    if int(calculation) == remember : break
    # 2-3. 기억하는 몸무게 값 추가
    remember += 1
# 3. 결과 출력
if not ans : print(-1)
else :
    for num in ans : print(num)