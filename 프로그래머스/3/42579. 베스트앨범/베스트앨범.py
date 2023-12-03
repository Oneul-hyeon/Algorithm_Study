from collections import defaultdict

def solution(genres, plays):
    answer = []
    # 1. 장르 딕셔너리 생성
    genre = defaultdict(list)
    for idx, g in enumerate(genres) :
        genre[g].append(idx)
    # 2. 장르 별 정렬
    information = list(genre.items())
    information.sort(key = lambda info : sum([plays[idx] for idx in info[1]]), reverse = True)
    print(information)
    # 3.
    for g, info in information :
        # 3-1. 재생 횟수 - 고유 번호 순으로 정렬
        info.sort(key = lambda x : -plays[x])
        # 3-2. 출력 리스트에 삽입
        answer += info[:2]
    # 4. 결과 리턴
    return answer