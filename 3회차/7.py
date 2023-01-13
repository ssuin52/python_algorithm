# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 실패
def solution(s):
    if s[0]==')' or s[-1]=='(':
        return False
    else:
        if s.count('(') == s.count(')'):
            return True
        else:
            return False

# 다른사람 코드
def solution(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0


def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        else:
            if stack==[]:
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False
print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))