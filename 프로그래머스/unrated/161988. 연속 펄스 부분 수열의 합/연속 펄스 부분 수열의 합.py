def solution(sequence):
    # 1. 2차원 구간 합 리스트 생성
    prefix_sum = [[0] * len(sequence) for _ in range(2)]
    # 2.펄스 변수 생성
    temp_0, temp_1 = 1, -1
    min_0 = min_1 = 0
    answer = -float('inf')
    # 3. 
    for i in range(len(sequence)) :
        # 3-1. 각 펄스에 맞게 누적합 생성 후 해당 인덱스 값에 저장
        if i == 0 :
            prefix_sum[0][i] = sequence[i] * temp_0
            prefix_sum[1][i] = sequence[i] * temp_1
        else :
            prefix_sum[0][i] = prefix_sum[0][i-1] + sequence[i] * temp_0
            prefix_sum[1][i] = prefix_sum[1][i-1] + sequence[i] * temp_1
        # 3-2. 결과값 업데이트
        answer = max(answer, prefix_sum[0][i] - min_0, prefix_sum[1][i] - min_1) if i > 0 else max(answer, prefix_sum[0][i], prefix_sum[1][i])
        # 3-3. 최솟값 업데이트
        min_0 = min(min_0, prefix_sum[0][i])
        min_1 = min(min_1, prefix_sum[1][i])
        # 3-4. 펄스 변환
        temp_0 *= -1
        temp_1 *= -1
    # 4. 결과 리턴
    return answer