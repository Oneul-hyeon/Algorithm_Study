import sys
from collections import Counter
input = sys.stdin.readline

length_w, length_s = map(int, input().split())
w, s = input().strip(), input().strip()
ans = 0

# 1. 단어 w의 Counter 생성
standard = Counter(w)
# 2.
for idx in range(length_w-1, length_s, 1):
    # 2-1. 인덱스가 -1일 경우
    if idx == length_w-1 :
        # 초기 후보 문자열 Counter 생성
        candidate = Counter(s[:length_w])
    # 2-2. 이외의 경우
    else :
        # Counter 업데이트
        delete_char, add_char = s[idx-length_w], s[idx]
        candidate[delete_char]-=1
        candidate[add_char]+=1
    # 2-3. 순열 체크 및 형태 업데이트
    ans+=(standard==candidate)
# 3. 형태의 갯수 출력
print(ans)