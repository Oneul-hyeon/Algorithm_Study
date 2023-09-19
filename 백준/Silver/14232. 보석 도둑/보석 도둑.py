import sys
input = sys.stdin.readline

def solution(k) :
    # 1. 출력 리스트 생성
    answer = []
    # 2.
    for i in range(2, int(k**0.5)+1) :
        # 2-1.
        while k % i == 0 :
            answer.append(i)
            k //= i
    # 3. 마지막 수가 소수인 경우 결과 리스트에 삽입
    if k != 1 :
        answer.append(k)
    # 3. 결과 출력
    print(len(answer))
    print(*answer)

if __name__ == '__main__' :
    k = int(input())
    solution(k)