# 평균 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12944

arr1 = [1, 2, 3,4]
arr2 = [5,5]

def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

print(solution(arr1))
print(solution(arr2))