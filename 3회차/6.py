# 가운데 글자 가져오기
# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s) % 2 == 1:
        answer = s[len(s)//2]
    else:
        answer = s[(len(s)//2)-1]+s[len(s)//2]
    return answer

def solution(s):
    return s[len(s)//2] if len(s) % 2 == 1 else s[(len(s)//2)-1]+s[len(s)//2]
    
# a='asdf'
# print(a[1])

print(solution('asdf'))

# 문자 리스트로 바꾸기