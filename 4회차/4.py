# 모의고사
#https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answers[i] == st1[(i%5)]:
            correct[0] += 1
        if answers[i] == st2[(i%8)]:
            correct[1] += 1
        if answers[i] == st3[(i%10)]:
            correct[2] += 1
    # return correct.index(max(correct))
    for i in range(3):
        if correct[i] == max(correct):
            answer.append(i+1)
    return answer

def solution(answers):
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5]
    correct = [0,0,0]
    answer=[]
    for i in range(len(answers)):
        if answers[i] == st1[(i%5)]:
            correct[0] += 1
        if answers[i] == st2[(i%8)]:
            correct[1] += 1
        if answers[i] == st3[(i%10)]:
            correct[2] += 1
    for idx, s in enumerate(correct):
        if s == max(correct):
            answer.append(idx+1)
    return answer

print(solution([1,2,3,4,5]))