# 실패율(2019 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 다시풀어보기!!!!

def solution(N, stages):
    answer=[]
    total = len(stages)

    fail_lst = []
    for i in range(1,N+1):
        num = stages.count(i)
        if num == 0: # 도달한 사람이 없으면 실패율 0
            fail_lst.append(0)
        else:
            fail_lst.append(num/total)
        total -= num # 전 스테이지에서 막히면 다음 스테이지에 도달 못하기 때문
    for i in range(N):
        idx = fail_lst.index(max(fail_lst))
        answer.append(idx+1)
        fail_lst[idx] = -1
    return answer
    
print(solution(5,[2,1,2,6,2,4,3,3]))