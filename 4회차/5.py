# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# def solution(k, dungeons):
#     answer = 0
#     for i in dungeons:
#         if k >= i[0]:
#             k = k-i[1]
#             answer += 1
#         else:
#             return answer
#     return answer

from itertools import permutations

def solution(k, dungeons):
    dunList = [i for i in permutations(dungeons, len(dungeons))] # 가능한 던전 순서 경우의 수
    answer = []
    for i in dunList:
        count = 0
        life = k # 최소 필요 피로도
        for j in i:
            if life >= j[0]:
                life = life-j[1]
                count += 1
        answer.append(count)
    return max(answer)

print(solution(80, [[80,20],[50,40],[30,10]]))