# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# def solution(s):
#     if s[0]==')' or s[-1]=='(':
#         return False
#     else:
#         if s.count('(') == s.count(')'):
#             return True
#         else:
#             return False
# def solution(s):
#     x = 0
#     for w in s:
#         if x < 0:
#             break
#         x = x+1 if w=="(" else x-1 if w==")" else x
#     return x==0

def solution(s):
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if arr == []:
                return False
            else:
                arr.pop()
    if arr != []:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))