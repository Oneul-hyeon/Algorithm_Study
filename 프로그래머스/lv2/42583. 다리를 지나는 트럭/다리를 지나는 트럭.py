def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0
    now_weight = 0
    # 큐 선언
    queue = deque()
    while truck_weights:
        # 경과 시간 체크
        answer += 1
        # 다리 통과한 경우
        if queue :
            for i in range(len(queue)) :
                queue[i][0] -= 1
            if queue[0][0] == 0 :
                now_weight -= queue.popleft()[1]
        # 트럭이 다리에 올라갈 수 있는 경우
        if now_weight + truck_weights[0] <= weight and len(queue) < bridge_length :
            queue.append([bridge_length, truck_weights.pop(0)])
            now_weight += queue[-1][1]
    return answer + queue[-1][0]