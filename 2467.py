import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
# 1. start, end 값 정하기
start, end = 0, n-1
# 2. 최솟값 변수 지정 -> [최솟값, start, end]
ans = [n * 1000000000 + 1, 0, 0]
# 3. while 문
while start < end :
    summation = array[start] + array[end]
    # 3-1. start+end 결과가 최솟값인지 확인
    if abs(summation) <= abs(ans[0]) :
        ans = [summation, start, end]
        if summation == 0 : break
    # 3-2. start + end 가 음수일 경우
    if summation < 0 : start += 1
    # 3-2. start + end 가 양수일 경우
    else : end -= 1
print(array[ans[1]], array[ans[2]])



