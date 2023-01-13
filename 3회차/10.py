# 다트게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# def solution(dartResult):
#     n=0
#     score=[]
#     for i in dartResult:
#         if i.isnumeric():
#             n += int(i)
#         elif i=='S':
#             n = int(n)**1
#             score.append(n)
#             n=0
#         elif i=='D':
#             n = int(n)**2
#             score.append(n)
#             n=0
#         elif i=='T':
#             n = int(n)**3
#             score.append(n)
#             n=0
#         elif i == '*':
#             if len(score) > 1: # 2개 이상일 때
#                 score[-2] = score[-2] * 2 # 직전 점수
#                 score[-1] = score[-1] * 2 # 해당 점수
#             else: # 1개 이하일 때
#                 score[-1] = score[-1] * 2
#         elif i == '#':
#             score[-1] = score[-1] * -1
#     return sum(score)


# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
# lst = ['a','s','d','de']
# # print(lst[-1])
# # print(lst[-2])


def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))