def solution(sticker):
    # 1. 스티커가 1개인 경우
    if len(sticker) == 1 : return sticker[0]
    # 2. DP 생성
    dp1 = [0] + sticker[:-1]
    dp2 = [0] + sticker[1:]
    # 3.
    for i in range(2, len(dp1)) :
        # 3-1. 0번 인덱스의 스티커를 뜯지 않은 dp 처리
        dp1[i] = max(dp1[i-2] + dp1[i], dp1[i-1])
        # 3-2. 0번 인덱스의 스티커를 뜯은 dp 처리
        dp2[i] = max(dp2[i-2] + dp2[i], dp2[i-1])
    # 4. 최댓값 출력
    return max(dp1[-1], dp2[-1])