def solution(key, lock):
    # 1. 열쇠 회전 함수 정의
    def rotate(key) :
        # 1-1. 90도 회전
        key = [list(line[::-1]) for line in zip(*key)]
        return key
    # 2. 열쇠 체크 함수 정의
    def check() :
        # 2-1.
        for i in range(n + m - 1) :
            for j in range(n + m - 1) :
                # 2-1-1.
                cnt = 0
                for l_x in range(m) :
                    for l_y in range(m) :
                        g_x, g_y = i - (m - 1) + l_x, j - (m - 1) + l_y
                        # 범위를 벗어날 경우 continue
                        if g_x < 0 or g_x >= n or g_y < 0 or g_y >= n : continue
                        # 돌기끼리 부딪힐 경우 고려 x
                        if lock[g_x][g_y] and key[l_x][l_y] : break
                        # 열쇠의 돌기가 자물쇠의 홈에 들어간 경우 카운팅
                        if lock[g_x][g_y] == 0 and key[l_x][l_y] == 1 : cnt += 1
                    # 2-1-2. 정상적으로 카운팅된 경우 자물쇠의 모든 홈을 막았다면 True 반환
                    else :
                        if cnt == lock_groove : return True
        # 2-2. False 반환
        return False
    m, n = len(key), len(lock)
    # 3. 열쇠의 돌기, 자물쇠의 홈 개수 체크
    key_protrusion, lock_groove = 0, 0
    for i in range(m) :
        for j in range(m) :
            if key[i][j] == 1 : key_protrusion += 1
    for i in range(n) :
        for j in range(n) :
            if lock[i][j] == 0 : lock_groove += 1
    # 4. 열쇠의 돌기 < 자물쇠의 홈 개수 일 경우 False 반환
    if key_protrusion < lock_groove : return False
    # 5. 이외의 경우
    else :
        # 5-1. 
        for i in range(4) :
            # 5-1-1. i > 0 일 경우 열쇠 회전
            if i > 0 : key = rotate(key)
            # 5-1-2. 열쇠로 자물쇠를 열 수 있을 경우 true 반환
            if check() : return True
        # 5-2. false 반환
        return False