# 다트게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    n=0
    score=[]
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i=='S':
            n = int(n)**1
            score.append(n)
            n=0
        elif i=='D':
            n = int(n)**2
            score.append(n)
            n=0
        elif i=='T':
            n = int(n)**3
            score.append(n)
            n=0
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)

