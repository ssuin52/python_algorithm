# 핸드폰 번호 가리기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    lst = phone_number[-4:]
    lst_len = len(phone_number)-4
    answer = []
    answer.append("*"*lst_len+lst)
    return ''.join(s for s in answer)
print(solution("01044412076"))

def solution2(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]
print(solution2("01044412076"))

# 슬라이싱 뒤에서부터 4개
# replace 사용 x

def solution(phone_number):
    lst=[]
    for i in phone_number[:-4]:
        lst.append("*")
    lst.append(phone_number[-4:])
    return ''.join(lst)
print(solution("01044412076"))