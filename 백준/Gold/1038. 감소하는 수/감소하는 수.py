import sys
from itertools import combinations
input = sys.stdin.readline

# 1. 출력 리스트 생성
ans = []
# 2.
for i in range(1, 11) :
    # 2-1.
    for combination in combinations(range(10), i) :
        # 2-1-1. 조합 내림차순 정렬 후 정수로 변환
        num = int(''.join([str(s) for s in sorted(combination, reverse = True)]))
        # 2-1-2. 출력 리스트에 삽입
        ans.append(num)
# 3. 출력 리스트 정렬
ans.sort()
# 4. 결과 출력
n = int(input())
print(ans[n] if n < len(ans) else -1)