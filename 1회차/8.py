# 약수의 개수와 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for a in range(left, right+1):
        lst=[]
        # 약수의 개수 구하기
        for i in range(1,a+1):
            if a % i == 0:
                lst.append(i)
        # 홀/짝 판별
        if len(lst)%2==0:
            answer += a
        else:
            answer -= a
    return answer

print(solution(13,17))
print(solution(24,27))


