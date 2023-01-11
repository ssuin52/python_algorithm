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

# 883.33ms
# 10.4mb

def solution(a,b):
    answer = 0
    for i in range(min(a,b), max(a,b)+1):
        answer += i
    return answer

# 984.63ms
# 10.3mb

def solution(a,b):
    answer = sum(range(a,b+1) if a<=b else range(b,a+1))
    return answer

# 330.65ms
# 10.3mb

print(solution(3,5))
print(solution(3,3))
print(solution(5,3))