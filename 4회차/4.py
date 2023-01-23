# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''
yellow의 가로를 x, 세로를 y라고 하면
전체 가로의 길이는 x+2, 세로는 y+2 를 구하면 된다.

1. yellow의 가로 세로 쌍을 구해서

2. brown = x*2 + y*2 +4 와 일치하는지 확인

3. 일치한다면 answer에 append
'''
def solution(brown, yellow):

    answer = []
    x = 0 #노랑이 가로
    y = 0 #노랑이 세로

    for i in range(1, yellow+1):
        if yellow % i == 0:
            x = int(yellow/i)# 가로가 세로보다 크거나 같기 때문
            y = i
            if x*2+y*2+4==brown:
                answer.append(x+2)
                answer.append(y+2)
                return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))