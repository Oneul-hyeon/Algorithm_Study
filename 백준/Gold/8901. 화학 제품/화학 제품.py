import sys
input = sys.stdin.readline

def solution(t):
    for _ in range(t) :
        a, b, c = map(int, input().split())
        ab, bc, ca = map(int, input().split())
        # 1. 출력값 변수 생성
        ans = 0
        # 2.
        for i in range(min(a, b) + 1) :
            for j in range(min(b-i, c) + 1) :
                # 2-1. 이익 계산
                value = i * ab + j * bc + min(a - i, c - j) * ca
                # 2-2. 최댓값 업데이트
                if value > ans :
                    ans = value
        # 3. 결과 출력
        print(ans)

if __name__ == "__main__" :
    t = int(input())
    solution(t)