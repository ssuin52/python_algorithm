# 두 정수 사이의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a,b):
    answer = 0
    if a <= b:
        for i in range(a, b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer += i
            
    return answer

print(solution(3,5))
print(solution(3,3))
print(solution(5,3))