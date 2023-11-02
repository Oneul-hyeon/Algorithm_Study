import sys
input = sys.stdin.readline

def solution(a, b) :
    # 1. 소수 판별 리스트, 거의 소수 리스트 생성
    end = int(b ** .5)
    decimal, ans = [True] * (end + 1), 0
    decimal[0], decimal[1] = False, False
    # 2.
    for i in range(2, end + 1) :
        # 2-1. 해당 수가 소수일 경우
        if decimal[i] :
            # 2-1-1.
            for j in range(i + i, end + 1, i) :
                # 소수 판별
                if decimal[j] : decimal[j] = False
    # 3.
    for i in range(1, end + 1) :
        n = 2
        if decimal[i] :
            while i ** n <= b :
                if i ** n >= a :
                    ans += 1
                n += 1
    # 4. 결과 출력
    print(ans)

if __name__ == "__main__":
    a, b = map(int, input().split())
    solution(a, b)