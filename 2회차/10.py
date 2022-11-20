# 소수 만들기(Summer/Winter Coding(~2018))
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations as cb
import sys
import math

# 소수 판별하기
def prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return None
    return x


def solution(nums):
    answer = 0
    lst = []
    for a in cb(nums,3):
        lst.append(sum(a))
    for j in lst:
        if prime_number(j):
            answer += 1
    return answer
        
print(solution([1,2,7,6,4]))
print(solution([1,2,3,4]))

# itertools의 combinations
