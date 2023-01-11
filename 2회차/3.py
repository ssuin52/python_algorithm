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

# 0.03ms
# 10.4mb


def solution2(n):
    string = [x for x in str(n)]
    string.sort(reverse=True)

    answer = ""

    for s in string:
        answer += s

    return int(answer)

# 0.04ms
# 10.4mb


def solution(n):
    lst = [x for x in str(n)]
    lst.sort(reverse=True)
    answer = int(''.join(i for i in lst))
    return answer

# 0.05ms
# 10.4mb

# 이자식 뭔데 자꾸 계속 오류나서 봤더니 마지막에 int로 안해줘서....부들부들.....
# sort와 reverse 정리하기

print(solution(118372))


def solution(n):
    answer =(''.join(sorted(str(n), reverse=True))) 
    return answer
print(solution(118372))    

# 문자열은 정렬이 되므로 list에 담아주지 않고 바로 정렬 가능
