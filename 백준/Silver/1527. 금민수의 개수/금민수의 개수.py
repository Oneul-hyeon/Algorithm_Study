import sys
from itertools import product
input = sys.stdin.readline

def solution(a, b) :
    # 1. 결과 변수 생성
    ans = 0
    # 2.
    for i in range(len(str(a)), len(str(b)) + 1) :
        # 2-1. 길이가 a 혹은 b의 길이와 같을 경우
        if i in [len(str(a)), len(str(b))] :
            for num in product([4, 7], repeat = i) :
                # 생성한 수가 범위 안에 들 경우 카운팅
                num = int(''.join(map(str, num)))
                if a <= num <= b : ans += 1
        # 2-2. 이외의 경우
        else :
            ans += 2**i
    # 3. 결과 출력
    print(ans)
    
if __name__ == '__main__' :
    a, b = map(int, input().split())
    solution(a, b)