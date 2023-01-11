# 같은 숫자는 싫어(스택/큐)
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i==0: 
            answer.append(arr[i]) # 첫번째 값 추가
        elif arr[i-1] != arr[i]: # 앞에 값과 일치하지 않으면 추가
            answer.append(arr[i])
    return answer

# 정확성 0.02ms, 10.3MB
# 효율성 125.09ms, 28MB

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))


# 스터디 팀원 코드
# 3. stack 사용 : 통과 (141.59ms, 21.8MB)
def solution(arr):
    answer = []
    while len(arr)>0:
        stack_pop = arr.pop()
        if(not answer or stack_pop != answer[-1]):
            answer.append(stack_pop)
    return list(reversed(answer))
    
print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))