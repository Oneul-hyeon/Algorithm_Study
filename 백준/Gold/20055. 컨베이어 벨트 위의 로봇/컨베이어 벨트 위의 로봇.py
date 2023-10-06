import sys
from collections import deque
input = sys.stdin.readline

def solution(n, k, belt) :
    # 1. 벨트 회전 함수 정의
    def rotate() :
        # 1-1. 컨베이어 벨트 회전
        belt.appendleft(belt.pop())
        # 1-2. 로봇 리스트 회전
        robot.appendleft(robot.pop())
        # 1-3. 내리는 위치에 로봇이 있을 경우 로봇 내리기
        if robot[-1] : robot[-1] = False
    # 2. 로봇 이동 함수 정의
    def move() :
        # 2-1.
        for i in range(n-2, -1, -1) :
            # 현재 칸에 로봇이 있으며 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상 남아있는 경우
            if robot[i] and not robot[i+1] and belt[i+1] > 0 :
                # 마지막 인덱스의 경우
                if i == n-2 :
                    # 현재 위치 로봇 제거
                    robot[i] = False
                # 이외의 경우
                else :
                    # 로봇 위치 변경
                    robot[i], robot[i+1] = robot[i+1], robot[i]
                # 내구도 감소
                belt[i+1] -= 1
    # 3. 로봇 올리기 함수
    def arrangement() :
        # 3-1. 올리는 위치의 내구도가 0보다 클 경우
        if belt[0] :
            # 로봇 올리기
            robot[0] = True
            # 내구도 감소
            belt[0] -= 1
    # 4. 내구도가 0인 칸의 개수 체크 함수
    def check() :
        return False if belt.count(0) >= k else True

    ans = 0
    belt = deque(belt)
    # 5. 로봇 리스트 생성
    robot = deque([False for _ in range(n)])
    # 6.
    while True :
        # 6-1. 벨트 회전
        rotate()
        # 6-2. 로봇 이동
        move()
        # 6-3. 로봇 올리기
        arrangement()
        # 6-4. 카운트
        ans += 1
        # 6-5. 체크
        if not check() : break
    # 7. 결과 출력
    print(ans)

if __name__ == "__main__" :
    n, k = map(int, input().split())
    belt = list(map(int, input().split()))
    solution(n, k, belt)