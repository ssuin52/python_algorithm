# 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            answer += i
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    if answer[0]=='.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer == '.'
    if answer[-1]=='.':
        answer = answer[:-1]
    
    # 5단계
    if len(answer)==0:
        answer = 'a'
    
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution('...!@BaT#*..y.abcdefghijklm.'))
print(solution('z-+.^.'))
print(solution('=.='))
print(solution('123_.def'))
print(solution('abcdefghijklmn.p'))