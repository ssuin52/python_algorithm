# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 다시풀어보기!!!!


def solution(n, lost, reserve):
    answer = 0
    reserve_st = []
    lost_st=[]
    reserve.sort() # 정렬필요
    for i in reserve:
        if i not in lost:
            reserve_st.append(i)
    for j in lost:
        if j not in reserve:
            lost_st.append(j)
    for a in reserve_st:
        if a-1 in lost_st:
            lost_st.remove(a-1)
        elif a+1 in lost_st:
            lost_st.remove(a+1)
    answer = n-len(lost_st)
    return answer

'''
정렬이 필요한 이유
n=5 reserve=[1, 3] lost=[2,4] 일 때
1번이 2번에게 빌려주고, 3번이 4번에게 빌려줄 수 있지만

n=5 reserve=[3, 1] lost=[2,4] 일 면
3번이 2번에게 빌려주고 4번은 체육복을 빌릴 수 없게된다.

때문에 최댓값을 반환하는 문제이므로 정렬이 필요하다
'''


def solution(n, lost, reserve):
    answer = 0
    # 중복값 제거 set()뺄셈 가능
    reserve_lst = list(set(reserve)-set(lost))
    lost_lst = list(set(lost)-set(reserve))
    for i in reserve_lst:
        if i-1 in lost_lst:
            lost_lst.remove(i-1)
        elif i+1 in lost_lst:
            lost_lst.remove(i+1)
    answer = n - len(lost_lst)
    return answer

# 0.01ms
# 10.3mb

# print(solution(5, [2, 4], [3]))
# print(solution(5, [2, 4], [1,3,5]))
# print(solution(3, [3], [1]))

lst = [1,4,5,6,3,2,6]
print(set(lst))
#{1, 2, 3, 4, 5, 6}