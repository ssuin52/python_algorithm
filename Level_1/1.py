# 2016년
# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a,b):
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = sum(month[:a-1])+b
    # date = 0
    # for i in range(a-1):
    #     print(i)
    #     date += month[i]
    # date += b
    answer = days[date%7-1]
    return answer
print(solution(5,24))
