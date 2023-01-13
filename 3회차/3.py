# 제일 작은 수 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr)==1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

print(solution([4,3,2,1]))

# arr와 lst 차이
