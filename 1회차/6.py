# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# 다시풀어보기!!!!

def solution(n, lost, reserve):
    answer = 0
    reserve_st = list(set(reserve) - set(lost))
    lost_st = list(set(lost) - set(reserve))
    for a in reserve_st:
        if a-1 in lost_st:
            lost_st.remove(a-1)
        elif a+1 in lost_st:
            lost_st.remove(a+1)
    answer = n-len(lost_st)
    return answer

# def solution(n, lost, reserve):
#     answer = 0
#     reserve_st = []
#     lost_st=[]
#     for i in reserve:
#         if i not in lost:
#             reserve_st.append(i)
#     print(reserve_st)
#     for j in lost:
#         if j not in reserve:
#             lost_st.append(j)
#     print(lost_st)
#     for a in reserve_st:
#         if a-1 in lost_st:
#             lost_st.remove(a-1)
#         elif a+1 in lost_st:
#             lost_st.remove(a+1)
#     answer = n-len(lost_st)
#     return answer

print(solution(5, [2, 4], [3]))
print(solution(5, [2, 4], [1,3,5]))
print(solution(3, [3], [1]))