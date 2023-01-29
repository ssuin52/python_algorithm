# 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product


def solution(word):
    lst = []
    for j in range(1,6):
        for i in list(product(['A','E','I','O','U'], repeat=j)):
            lst.append(''.join(i))
    lst.sort()
    return lst.index(word)+1

print(solution('A'))

