import sys
from collections import deque
input = sys.stdin.readline

# 1. 재귀함수 선언
def dfs(index) :
    if index == len(permutation) :
        if max(array) == n:
            print(*array)
            sys.exit()
        return
    if int(permutation[index]) > 0 and int(permutation[index]) not in array:
        # 3. 재귀 함수 실행(1자리 수)
        array.append(int(permutation[index]))
        dfs(index+1)
        array.pop()
    if index+1 < len(permutation) :
        if 0< int(permutation[index : index +2]) <= n and int(permutation[index : index +2]) not in array:
            # 4. 재귀 함수 실행(2자리 수)
            array.append(int(permutation[index : index +2]))
            dfs(index+2)
            array.pop()

# 5. 순열 입력받기
permutation = input().rstrip()
# 6. N 구하기
if len(permutation) <= 9 : n = len(permutation)
else : n = 9 + (len(permutation) - 9)//2
# 7. 기준 리스트 설정
stand_array = set([str(x) for x in range(1, n+1)])
array = deque()
# 8. 재귀 함수 실행
dfs(0)
