# 예산(Summer/Winter Coding(~2018))
# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    count = 0
    d.sort()
    for i in d:
        if i <= budget:
            budget -= i
            count += 1
    return count

# 0.02ms
# 10.2MB

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))