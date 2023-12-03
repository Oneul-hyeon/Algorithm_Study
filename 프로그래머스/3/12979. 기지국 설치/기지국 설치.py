def solution(n, stations, w):
    answer = 0
    # 1. left 값 초기 설정
    left = 1
    # 2. 
    for station in stations :
        # 2-1. right 값 구하기
        right = station - w - 1
        # 2-2. 증설해야 하는 기지국 카운팅
        if right >= left : answer += (right - left + 1) // (2 * w + 1) if (right - left + 1) % (2 * w + 1) ==0 else (right - left + 1) // (2 * w + 1) + 1
        print(answer)
        # 2-3. left 값 재설정
        left = station + w + 1
    # 3. 증설해야 하는 기지국 카운팅
    if left <= n :
        answer += (n - left + 1) // (2 * w + 1) if (n - left + 1) % (2 * w + 1) == 0 else (n - left + 1) // (2 * w + 1) + 1
    # 4. 결과 리턴
    return answer