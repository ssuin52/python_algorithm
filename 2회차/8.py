# 같은 숫자는 싫어(스택/큐)
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0:
            answer.append(arr[i])
        elif arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

# arr = [1,1,3,3,0,1,1]

# print(arr[0])
# print(len(arr)-1)
# for i in range(len(arr)-1):
#     if arr[i] != arr[i+1]:
#         print