import sys
input = sys.stdin.readline

def solution(n, info) :
    # 1. 출력 변수 생성
    answer = 0
    # 2.
    for i in range(1, n) :
        # 2-1. 와이어 설치 비용 더하기
        answer += (info[i-1] + info[i]) ** 2 + (info[i-1] - info[i]) ** 2
    # 3. 결과 출력
    print(answer)
    
if __name__ == "__main__" :
    n = int(input())
    info = list(map(int, input().split()))
    solution(n, info)