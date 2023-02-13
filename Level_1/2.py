# 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer=[]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer

# 간단하게 정리하기
def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    answer.sort()
    return answer if len(answer) != 0 else [-1]

print(solution([5,9,7,10],5))
print(solution([3,2,6],10))