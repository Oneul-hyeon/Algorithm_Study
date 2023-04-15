import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n, m = map(int, input().split())
# 1. 리스트에 강의 담기
array = list(map(int, input().split()))

# 2. start, end 설정
start, end = max(array), sum(array)
# 3. while문
while start <= end :
    # 3-1. count, mid 변수 정의
    count, summation = 0, 0
    mid = (start + end) // 2
    # 3-2. 해당 블루레이의 크기에 따라 카운트된 개수가 m개인지 확인
    for i in array :
        if summation + i > mid :
            count += 1
            summation = 0
        summation += i
    count += 1 if summation else 0

    # 3-3. count > m 일 때
    if count > m : start = mid+1
    # 3-4. count < m 일 때
    else : end = mid - 1
print(start)


