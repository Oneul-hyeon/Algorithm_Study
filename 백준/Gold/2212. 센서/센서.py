import sys
input = sys.stdin.readline

n, k = int(input()), int(input())
if n <= k : print(0)
else:
    # 1. 센서의 좌표 정렬
    sensor_index = sorted(list(map(int, input().split())))
    # 2. 센서 간 거리 리스트 생성해 내림차순으로 정렬
    distances = sorted([sensor_index[i+1] - sensor_index[i] for i in range(n-1)], reverse = True)
    # 3. 거리가 큰 값 삭제(k-1개 만큼)
    answer = sum(distances) - sum(distances[i] for i in range(k-1))
    # 4. 나머지 합 출력
    print(answer)