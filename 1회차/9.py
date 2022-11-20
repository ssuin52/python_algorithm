# 없는 숫자 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/86051

# 리스트 빼기 안됨
# set으로 바꿔서 빼준다음 원소 더해주자
def solution1(numbers):
    all = [0,1,2,3,4,5,6,7,8,9]
    answer_list = list(set(all)-set(numbers))
    answer = 0
    for i in answer_list:
        answer += i
    return answer

print(solution1([5,8,4,0,6,7,9]))

# all 리스트에 0~9까지 넣어주고 numbers에 없는 원소만 빼서 더해주자
def solution2(numbers):
    answer = 0
    all = [0,1,2,3,4,5,6,7,8,9]
    for i in all:
        if i not in numbers:
            answer += i
    return answer

print(solution2([1,2,3,4,6,7,8,0]))
    
