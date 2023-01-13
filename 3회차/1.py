# 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    str = s.lower()
    if str.count("p")==str.count("y"):
        return True
    return False

print(solution("pPoooyY"))
print(solution("pyY"))


def solution(s):
    return True if s.lower().count('p')==s.lower().count('y') else False

print(solution("pPoooyY"))
print(solution("pyY"))


def solution2(s):
    return s.lower().count("p")==s.lower().count("y")

print(solution2("pPoooyY"))
print(solution2("pyY"))

# lower()
# count()

