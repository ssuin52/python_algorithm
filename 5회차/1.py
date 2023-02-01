# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
from itertools import product

def solution(numbers, target):
    num_lst = [(x, -x) for x in numbers]
    pd_num = list(product(*num_lst))
    count = 0
    for i in pd_num:
        if sum(i) == target:
            count += 1
    return count

print(solution([4, 1, 2, 1],4))