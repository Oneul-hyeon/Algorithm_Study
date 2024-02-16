import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

# 1. 숫자 우선 배치 딕셔너리, 매핑용 딕셔너리 생성
priority_number, mapping_number = defaultdict(int), defaultdict(int)
# 2.
for i in range(max([len(word) for word in words])) :
    # 2-1.
    for word in words :
        # 2-1-1. 처리가 가능한 경우
        if len(word) > i :
            # 숫자 우선 배치 딕셔너리 업데이트
            priority_number[word[::-1][i]] += 2*10**i
# 3.
num = 9
for key, value in sorted(priority_number.items(), key = lambda x : -x[1]) :
    # 매핑용 딕셔너리 업데이트
    mapping_number[key] = str(num)
    num -= 1
# 4.
ans = 0
for word in words :
    # 숫자 변환 후 출력 변수 업데이트
    number = ''
    for i in range(len(word)) : number += mapping_number[word[i]]
    ans += int(number)
# 5. 결과 출력
print(ans)