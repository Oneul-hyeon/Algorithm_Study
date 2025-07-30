import sys
input = sys.stdin.readline

_ = input()
array = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
# 1.
for a in array:
    # 1-1. 필요 감독관 수 업데이트
    # 1-1-1. 총 감독관의 감시 가능 응시자 수가 현재 시험장의 응시자 수보다 많은 경우
    if a > b:
        ans += 1 + (remain:=a-b)//c + (remain%c>0)
    # 1-1-2. 이외의 경우
    else :
        ans += 1
# 2. 결과 출력
print(ans)