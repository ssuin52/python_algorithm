#키패드 누르기
#https://school.programmers.co.kr/learn/courses/30/lessons/67256

# 거리계산 실패
# def solution(numbers, hand):
#     answer = ''
#     left_stack = ['*']
#     right_stack = ['#']
#     for number in numbers:
#         if number in [1,4,7]:
#             answer += 'L'
#             left_stack.append(number)
#         elif number in [3,6,9]:
#             answer += 'R'
#             right_stack.append(number)
#         else:
#             a = left_stack.pop()
#             b = right_stack.pop()
#
#     return answer

import math

def solution(numbers, hand):
    answer=''
    #키패드 위치
    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    left_pad = pad['*']   #처음 왼손의 위치
    right_pad = pad['#']  #처음 오른손의 위치

    for number in numbers:
        # 무조건 왼손
        if number in [1,4,7]:
            answer += 'L'
            left_pad = pad[str(number)]
        # 무조건 오른손
        elif number in [3,6,9]:
            answer += 'R'
            right_pad = pad[str(number)]
        # 거리계산 필요    
        else:
           # 점과 점 사이의 거리
            left_d = math.ceil(math.sqrt(math.pow((pad[str(number)][0]-left_pad[0]),2)+math.pow((pad[str(number)][1]-left_pad[1]),2)))
            right_d = math.ceil(math.sqrt(math.pow((pad[str(number)][0]-right_pad[0]),2)+math.pow((pad[str(number)][1]-right_pad[1]),2)))
            #번호와 왼손의 거리 계산
            left_d = abs(left_pad[0] - pad[str(number)][0]) + abs(left_pad[1] - pad[str(number)][1])
            #번호와 오른손의 거리 계산
            right_d = abs(right_pad[0] - pad[str(number)][0]) + abs(right_pad[1] - pad[str(number)][1])

            
            if left_d < right_d:
                answer += 'L'
                left_pad = pad[str(number)]
            elif left_d > right_d:
                answer += 'R'
                right_pad = pad[str(number)]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pad = pad[str(number)]
                else:
                    answer += 'R'
                    right_pad = pad[str(number)]
    return answer



print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))

