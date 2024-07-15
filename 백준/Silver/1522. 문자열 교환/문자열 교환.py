import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

string = input().strip()

# 1. 윈도우 사이즈 설정
window_size = string.count("a")
# 2. a가 없을 경우 0 출력
if window_size == 0 : print(0)
# 3. 이외의 경우
else :
    # 3-1. 순환 문자열 생성
    string += string
    # 3-2. 문자별 카운트 딕셔너리 생성
    count = {"a" : 0, "b" : 0}
    # 3-3. 초기값 설정
    for s in string[:window_size] : count[s] += 1
    # 3-4.
    ans = float("INF")
    for end in range(window_size, len(string)) :
        start = end - window_size + 1
        # 3-4-1. 문자별 카운트 딕셔너리 업데이트
        count[string[start-1]] -= 1
        count[string[end]] += 1
        # 3-4-2. 최솟값 업데이트
        ans = min(ans, count["b"])
    # 3-5. 결과 출력
    print(ans)