import sys
from collections import deque
input = sys.stdin.readline

# 1. 톱니바퀴 회전 함수 선언
def rotate() :
    #
    for i in range(1, 5) :
        if check[i][0] :
            # 1-1. 반시계 방향으로 회전
            if check[i][1] == -1 : gear[i].append(gear[i].popleft())
            # 1-2. 시계 방향으로 회전
            else : gear[i].appendleft(gear[i].pop())

# 2. 톱니바퀴 입력받기
gear = [[]]
for _ in range(4) : gear.append(deque(list(map(int, str(input().rstrip())))))
k = int(input())
for _ in range(k) :
    # 3. 회전시킨 톱니바퀴의 번호, 방향 입력받기
    num, dir = map(int, input().split())
    # 4. 톱니바퀴 별 회전 여부 리스트 생성
    check = [[False, 1] for _ in range(5)]
    # 5. 해당 번호 톱니바퀴 회전 여부 입력
    check[num] = [True, dir]
    # 6.
    for i in range(num, 1, -1) :
        # 6-1. 현재 톱니바퀴의 6번 인덱스와 다음 톱니바퀴의 2번 인덱스가 다를 경우 반대 방향으로 회전 여부 입력
        if gear[i][6] != gear[i-1][2] :
            check[i-1] = [True, check[i][1] * -1]
        # 6-2. 이외의 경우 for 문 탈출
        else : break
    # 7.
    for i in range(num, 4) :
        # 7-1. 현재 톱니바퀴의 2번 인덱스와 다음 톱니바퀴의 6번 인덱스가 다를 경우 반대 방향으로 회전 여부 입력
        if gear[i][2] != gear[i+1][6] :
            check[i+1] = [True, check[i][1] * -1]
        # 7-2. 이외의 경우 for 문 탈출
        else : break
    # 8. 톱니바퀴 회전
    rotate()
# 9. 점수의 합 출력
print(gear[1][0] * 1 + gear[2][0] * 2 + gear[3][0] * 4 + gear[4][0] * 8)