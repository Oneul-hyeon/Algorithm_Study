import sys
input = sys.stdin.readline

def solution(n):
    # 1. 주어진 수가 2나 5로 나눠질 경우
    if n % 2 == 0 or n % 5 == 0 : print(-1)
    # 2. n이 1일 경우
    elif n == 1 : print(1)
    # 3. 이외의 경우
    else :
        # 3-1. 시작값 설정
        x = 1
        # 3-2. 자릿수 변수 설정
        digit = 1
        # 3-3.
        while x != 0 :
            # 값에 다음 자릿수 값을 n으로 나눈 나머지 더하기
            x += (x * 9 + 1) % n
            # x값 재정의
            x %= n
            # 자릿수 값 카운트
            digit += 1
        # 3-4. 결과 출력
        print(digit)

if __name__ == "__main__":
    n = int(input())
    solution(n)