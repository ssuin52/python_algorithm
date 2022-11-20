# 음양 더하기(월간 코드 챌린지 시즌 2)
# https://school.programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# print(solution([4,7,12],[true,false,true]))

# abs = [4,7,2]
# for i in abs:
#     print(i)
