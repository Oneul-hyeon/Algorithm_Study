import sys
input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))

# 1. 총 나무의 희망 높이의 합이 3의 배수가 아닐 경우 NO 출력
if (total_sum := sum(trees)) % 3 : print("NO")
# 2. 총 나무의 희망 높이의 합이 3일 경우
else :
    # 2-1. 높이를 2 성장시키는 물뿌리개의 사용 가능 횟수가 총 나무의 희망 높이의 합을 3으로 나눈 몫보다 크거나 같은 경우
    if sum([height // 2 for height in trees]) >= total_sum // 3 :
        # YES 출력
        print("YES")
    # 2-2. 이외의 경우
    else :
        # NO 출력
        print("NO")