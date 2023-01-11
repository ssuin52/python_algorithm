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

# 0.15ms 
# 10.3MB


def solution(absolutes, signs):
    answer = sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(absolutes))])
    return answer

# 0.16ms
# 10.3MB

print(solution([4,7,12],[True,False,True]))


def solution(absolutes, signs):
    return sum([x if signs[i] else -x for i,x in enumerate(absolutes)])
