import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution(n) :
    # 1. 최대 힙, 최소 힙 조정 함수 정의
    def adjustment() :
        # 1-1. 최대 힙, 최소 힙의 길이 구하기
        l, r = len(LEFT_HEAP), len(RIGHT_HEAP)
        # 1-2. 현재까지 숫자의 갯수가 홀수 개인 경우
        if (l+r) % 2 != 0 :
            while l != r + 1 :
                if l > r + 1 :
                    heappush(RIGHT_HEAP, -heappop(LEFT_HEAP))
                    l -= 1
                    r += 1
                else :
                    heappush(LEFT_HEAP, -heappop(RIGHT_HEAP))
                    l += 1
                    r -= 1
        # 1-3. 현재까지 숫자의 갯수가 짝수 개인 경우
        else :
            while l != r :
                if l > r :
                    heappush(RIGHT_HEAP, -heappop(LEFT_HEAP))
                    l -= 1
                    r += 1
                else :
                    heappush(LEFT_HEAP, -heappop(RIGHT_HEAP))
                    l += 1
                    r -= 1
    # 2. 최대 힙, 최소 힙 생성
    LEFT_HEAP, RIGHT_HEAP = [], []
    # 3.
    for _ in range(n) :
        num = int(input())
        # 3-1. 첫 번째 수를 최대 힙에 삽입
        if not LEFT_HEAP and not RIGHT_HEAP : heappush(LEFT_HEAP, -num)
        else :
            # 입력받은 수가 중간값보다 작거나 같을 경우 최대 힙에, 클 경우 최소 힙에 삽입
            if num <= -LEFT_HEAP[0] : heappush(LEFT_HEAP, -num)
            else : heappush(RIGHT_HEAP, num)
            # 조정 수행
            adjustment()
        # 중간값 출력
        print(-LEFT_HEAP[0])

if __name__ == "__main__" :
    n = int(input())
    solution(n)