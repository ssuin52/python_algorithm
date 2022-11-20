# 정수 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12933



def solution(n):
    lst = []
    for i in str(n):
        lst.append(i)
    lst.sort()
    lst.reverse()
    answer = int(''.join(lst))
    return answer


def solution2(n):
    string = [x for x in str(n)]
    string.sort(reverse=True)

    answer = ""

    for s in string:
        answer += s

    return int(answer)



# 이자식 뭔데 자꾸 계속 오류나서 봤더니 마지막에 int로 안해줘서....부들부들.....
# sort와 reverse 정리하기

print(solution(118372))