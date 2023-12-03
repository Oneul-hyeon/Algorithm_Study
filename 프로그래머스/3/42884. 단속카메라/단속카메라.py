def solution(routes):
    answer = 1
    # 1. 차량의 경로 정렬하기
    routes.sort()
    # 2. 카메라 설치 포인트 지정
    camera = routes[0][1]
    # 3.
    for s, e in routes[1:] :
        # 3-1. 현재 차량의 이동 경로가 기준을 벗어난 경우
        if camera < s :
            # 카운팅
            answer += 1
            # 기준 재지정
            camera = e
        # 3-2. 기준을 벗어나지 않은 경우
        camera = min(camera, e)
    # 4. 결과 리턴
    return answer