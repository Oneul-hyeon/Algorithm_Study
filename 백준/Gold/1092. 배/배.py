import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
weights = list(map(int, input().split()))

# 1. 짐을 나를 수 없는 경우
if max(crane) < max(weights) : print(-1)
# 2. 이외의 경우
else :
    # 2-1. 크레인 역정렬
    crane.sort(reverse = True)
    # 2-2. 짐 역정렬
    weights.sort(reverse = True)
    # 2-3. 출력 변수 생성
    ans = 0
    # 2-4.
    while weights :
        # 2-4-1. 출력 변수 업데이트
        ans += 1
        # 2-4-2.
        for crane_idx, c in enumerate(crane) :
            for weight_idx, weight in enumerate(weights) :
                # 만약 크레인이 해당 짐을 들 수 있을 경우
                if c >= weight :
                    # 짐 제거
                    weights.pop(weight_idx)
                    break
    # 2-5. 결과 출력
    print(ans)