# 제일 작은 수 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr)==1:
        answer = [-1]
    else:
        a = min(arr)
        arr.remove(a)
        answer = arr
    return answer

print(solution([4,3,2,1]))

# print(len([1,2,3]))

# arr와 lst 차이