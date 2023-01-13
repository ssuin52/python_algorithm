# 수박수박수박수박수박수?
# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    if n % 2 == 0:
        answer = n//2 * '수박'
    else:
        answer = n//2 * '수박' + '수'
    return answer

def solution(n):
    return n//2 * '수박' if n%2==0 else n//2 * '수박' + '수'
    
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

print(solution(3))