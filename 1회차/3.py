# 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12931

# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수



def solution(n):
    answer=0
    num = str(n)
    for i in num:
        answer += int(i)
    return answer

def solution2(n):
    answer = 0
    while n > 10:
        a = n % 10 #나머지
        b = n // 10 #몫
        answer += a
        n = b
        if n < 10:
            return answer+n

print(solution(987))
print(solution(123))
print(solution(100))
print(solution(10))