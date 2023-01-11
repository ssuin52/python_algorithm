# K 번째 수(정렬)
# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for i in commands:
        lst = array[i[0]-1:i[1]]
        lst.sort()
        answer.append(lst[i[2]-1])
    return answer

# 0.01ms
# 10.3mb

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 슬라이싱, sort 정리

# sorted