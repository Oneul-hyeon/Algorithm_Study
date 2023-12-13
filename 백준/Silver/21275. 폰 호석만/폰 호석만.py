import sys
input = sys.stdin.readline
def solution(a, b):
    # 1. 출력 리스트 생성
    answer = []
    # 2.
    for A in range(2, 37) :
        # 2-1.
        try :
            # A 구하기
            AX = int(a, A)
        # 2-2.
        except : continue
        # 2-3. X가 2^63 이상일 경우 continue
        if AX >= 2** 63 : continue
        # 2-4.
        for B in range(2, 37) :
            # 2-4-1. A와 B가 같을 경우 continue
            if A == B : continue
            # 2-4-2.
            try :
                # B 구하기
                BX = int(b, B)
            # 2-4-3.
            except : continue
            # 2-4-4. X가 같을 경우 출력 리스트에 값 삽입
            if AX == BX :
                answer.append((AX, A, B))
    # 3. 결과 출력
    if not answer : print("Impossible")
    elif len(answer) > 1 : print("Multiple")
    else : print(*answer[0])

if __name__ == "__main__" :
    a, b = map(str, input().rstrip().split())
    solution(a, b)