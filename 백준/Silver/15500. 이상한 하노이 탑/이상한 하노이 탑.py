import sys
from collections import deque
input = sys.stdin.readline

def solution(n, pole_1) :
    pole_2, ans = deque(), []
    # 2. 원판 딕셔너리 생성 후 정보 입력
    disk = {i : 1 for i in range(1, n+1)}
    # 3.
    for i in range(n, 0, -1) :
        # 3-1.
        while True :
            # 3-1-1. 가장 위에 있는 원판이 목표 원판인 경우
            if (disk[i] == 1 and pole_1[-1] == i) or (disk[i] == 2 and pole_2[-1] == i) :
                if disk[i] == 1 :
                    pole_1.pop()
                    ans.append((1, 3))
                else :
                    pole_2.pop()
                    ans.append((2, 3))
                break
            # 3-1-2. 이외의 경우
            else :
                if disk[i] == 1 :
                    num = pole_1.pop()
                    disk[num] = 2
                    pole_2.append(num)
                    ans.append((1, 2))
                else :
                    num = pole_2.pop()
                    disk[num] = 1
                    pole_1.append(num)
                    ans.append((2, 1))
    # 3. 결과 출력
    print(len(ans))
    for line in ans :
        print(*line)
if __name__ == "__main__":
    n = int(input())
    # 1. 1번 장대 리스트 입력
    pole_1 = deque(map(int, input().split()))
    solution(n, pole_1)