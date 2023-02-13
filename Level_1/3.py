# 문자열 내 마음대로 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    lst=[]
    answer=[]
    for i in strings:
        i = i[n]+i
        lst.append(i)
    lst.sort()
    for j in lst:
        j = j[1:]
        answer.append(j)
    return answer


# 간단하게 정리하기
def solution(strings, n):
    lst = [i[n]+i for i in strings]
    lst.sort()
    answer = [j[1:] for j in lst]
    return answer

print(solution(["sun", "bed", "car"],1))