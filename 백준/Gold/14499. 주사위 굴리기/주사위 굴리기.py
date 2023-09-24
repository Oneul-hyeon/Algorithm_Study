import sys
input = sys.stdin.readline

def solution(n, m, x, y, graph, commands) :
    # 1. 주사위 위치변경 함수 정의
    def move_dice(command) :
        # 1-1. 주사위를 동쪽으로 굴릴 때
        if command == 1 : dice['top'], dice['right'], dice['left'], dice['bottom'] = dice['right'], dice['bottom'], dice['top'], dice['left']
        # 1-2. 주사위를 서쪽으로 굴릴 떄
        elif command == 2 : dice['top'], dice['right'], dice['left'], dice['bottom'] = dice['left'], dice['top'], dice['bottom'], dice['right']
        # 1-3. 주사위를 북쪽으로 굴릴 떄
        elif command == 3:
            dice['top'], dice['rare'], dice['front'], dice['bottom'] = dice['rare'], dice['bottom'], dice['top'], dice['front']
        # 1-4. 주사위를 남쪽으로 굴릴 때
        else :
            dice['top'], dice['rare'], dice['front'], dice['bottom'] = dice['front'], dice['top'], dice['bottom'], dice['rare']
        return

    dice = {}
    for d in ['top', 'rare', 'right', 'left', 'front', 'bottom'] : dice[d] = 0
    # 2. 방향 변수 설정
    dirs = [[], (0, 1), (0, -1), (-1, 0), (1, 0)]
    # 3.
    for command in commands :
        nx, ny = x + dirs[command][0], y + dirs[command][1]
        # 3-1. 예외처리
        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        # 3-2. 주사위 위치 변경
        move_dice(command)
        # 3-3. 주사위의 윗면에 쓰인 수 출력
        print(dice['top'])
        # 3-4. 이동한 칸에 쓰여 있는 수가 0 인 경우
        if graph[nx][ny] == 0 :
            graph[nx][ny] = dice['bottom']
        # 3-5. 이동한 칸에 쓰여 있는 수가 0이 아닌 경우
        else :
            dice['bottom'] = graph[nx][ny]
            graph[nx][ny] = 0
        # 3-6. 위치 재설정
        x, y = nx, ny
    return
if __name__ == '__main__' :
    n, m, x, y, _ = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    commands = list(map(int, input().split()))
    solution(n, m, x, y, graph, commands)