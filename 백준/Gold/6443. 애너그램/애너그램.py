import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(cnt, string) :
    # 1-1. 종료 조건 설정
    if cnt == StrLen :
        print(f"{string}")
        return
    # 1-2.
    for key in words.keys() :
        # 1-2-1. 해당 단어가 남는 경우
        if words[key] :
            # 단어 수 감소
            words[key] -= 1
            # 백트래킹 실행
            backtracking(cnt+1, string + key)
            # 단어 수 증가
            words[key] += 1

n = int(input())
# 2.
for _ in range(n) :
    # 2-1. 단어 정렬
    word = sorted(list(input().strip()))
    # 2-2. 단어 딕셔너리 생성
    words = {}
    for w in word :
        try : words[w] += 1
        except : words[w] = 1
    StrLen = len(word)
    # 2-3. 백트래킹 실행
    backtracking(0, "")