import sys, bisect
input = sys.stdin.readline

def solution(n, array) :
    # 1. LIS 리스트 생성
    LIS = []
    # 2.
    for i in array :
        # 2-1. 리스트가 비었거나 리스트의 마지막 수가 현재 수보다 작을 경우 현재 수 삽입
        if not LIS or LIS[-1] < i : LIS.append(i)
        # 2-2. 이외의 경우
        else :
            idx = bisect.bisect_left(LIS, i)
            LIS[idx] = i
    # 3. 결과 출력
    print(n - len(LIS))

if __name__ == "__main__":
    n = int(input())
    array = [int(input()) for _ in range(n)]
    solution(n, array)