import sys
from collections import defaultdict
input = sys.stdin.readline

def solution():
    # 1. 딕셔너리 생성
    case = defaultdict(int)
    # 2.
    for _ in range(int(input())) :
        # 2-1. 입력된 문자의 양 끝을 제외한 나머지 정렬
        string = list(input().rstrip())
        if len(string) > 2 : string = [string[0]] + sorted(string[1:-1]) + [string[-1]]
        # 2-2. 매핑된 값 추가
        case[tuple(string)] += 1
    # 3.
    for _ in range(int(input())) :
        # 3-1. 문장 입력받기
        sentence = list(map(str, input().rstrip().split()))
        # 3-2. 각 단어 정렬
        for idx, word in enumerate(sentence) :
            if len(word) > 2: sentence[idx] = [word[0]] + sorted(word[1:-1]) + [word[-1]]
        # 3-3.
        answer = 0
        for idx, c in enumerate(sentence) :
            if idx == 0 :
                answer = case[tuple(c)]
            else :
                answer *= case[tuple(c)]
        # 3-4. 결과 출력
        print(answer)

if __name__ == "__main__" :
    solution()