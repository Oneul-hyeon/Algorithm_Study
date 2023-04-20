import sys
from itertools import combinations
input = sys.stdin.readline

n, m, k = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(m)]
skills_combination = combinations(list(range(1, 2*n +1)), n)
max_count = -int(1e9)
for skills in skills_combination :
    count = 0
    for quest in quests :
        if set(quest) & set(skills) == set(quest) : count += 1
    if max_count < count : max_count = count
print(max_count)