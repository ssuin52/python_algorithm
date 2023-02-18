# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    corr_count = 0    
    zero_count = 0
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            corr_count += 1
        if lottos[i] == 0:
            zero_count += 1

    max_count = zero_count + corr_count
    answer = [rank[max_count],rank[corr_count]]
    return answer


print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]