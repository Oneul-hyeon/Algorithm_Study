def solution(n, times):
    # 1. left, right 설정
    left, right = 1, n * max(times)
    # 2.
    while left <= right :
        # 2-1. mid 값 설정
        mid = (left + right) // 2
        # 2-2. 해당 시간 동안 입국 심사를 받을 수 있는 사람 수 체크
        count = 0
        for time in times : count += mid // time
        # 2-3. 입국 심사를 받을 수 있는 사람 수가 n 보다 적을 경우
        if count < n : left = mid + 1
        # 2-4. 입국 심사를 받을 수 있는 사람 수가 n 보다 많거나 같을 경우
        else : right = mid - 1
    # 3. 결과 리턴
    return left