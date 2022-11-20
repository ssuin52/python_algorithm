# 예산(Summer/Winter Coding(~2018))
# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
    return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))

# 