import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    # 1. default dictionary 생성
    information = defaultdict(list)
    # 2.
    for idx, s in enumerate(s:=input().strip()):
        # 2-1. 문자 별 인덱스 정보 삽입
        information[s].append(idx)
    # 3.
    k = int(input())
    min_ans, max_ans = float("inf"), -float("inf")
    for key, value in information.items():
        # 3-1. value 길이가 k 이상인 경우
        if (length:=len(value)) >= k:
            # 3-2.
            for idx in range(length-k+1):
                # 3-2-1. 최소 문자열 길이 업데이트
                min_ans=min(min_ans, (sub:=value[idx+k-1]-value[idx]+1))
                # 3-2-2. 최대 문자열 길이 업데이트
                max_ans=max(max_ans, sub)
    # 4. 결과 출력
    print(-1 if float("inf") in [min_ans, -max_ans] else f"{min_ans} {max_ans}")