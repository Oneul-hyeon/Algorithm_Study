import sys
input = sys.stdin.readline

n = int(input())
_ = int(input())
array = list(map(int, input().split()))
# 1. 사진틀 리스트 생성
candidates = [[], []]
# 2.
for student in array :
    # 3. 비어 있는 사진틀이 있는 경우
    if len(candidates[0]) < n :
        if student in candidates[0] :
            candidates[1][candidates[0].index(student)] += 1
        else :
            # 3-1. 추천받은 학생의 사진 게시
            candidates[0].append(student)
            candidates[1].append(1)
    # 4. 비어 있는 사진틀이 없는 경우
    else :
        # 4-1. 현재 추천받은 학생이 사진틀에 없는 경우
        if student not in candidates[0] :
            # 4-1-1. 현재까지 추천받은 횟수가 가장 적은 학생의 사진 삭제
            min_recommendation = min(candidates[1])
            # 4-1-2. 추천받은 횟수가 가장 적은 학생이 두 명 이상일 경우 처리
            remove_index = candidates[1].index(min_recommendation)
            candidates[0].pop(remove_index)
            candidates[1].pop(remove_index)
            # 4-1-3. 새롭게 추천받은 학생의 사진 게시
            candidates[0].append(student)
            candidates[1].append(1)
        # 4-2. 현재 추천받은 학생이 사진틀에 있는 경우
        else :
            # 4-2-1. 추천받은 횟수만 증가
            candidates[1][candidates[0].index(student)] += 1
print(*sorted(candidates[0]))