# 나머지가 1이 되는 수 찾기(월간 코드 챌린지 시즌 3)
# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(1,n):
        if n % i == 1:
            answer = i
            break
    return answer
# 86.53ms 
# 10.1MB


def solution(n):
    for i in range(1,n):
        if n%i == 1:
            return i

# 61.69ms 
# 10.2MB


def solution(n):
    answer = [i for i in range(1, n) if n % i == 1][0]
    return answer

# 54.29ms 
# 10.2MB

print(solution(10))