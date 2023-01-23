# 소수찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 내 풀이
def solution(n):
    count = 0
    for i in range(2, n+1):
        for a in range(2, int(i**(1/2))+1):
            if i % a == 0:
                break
        else:
            count += 1
    return count


# 다른 사람의 풀이 / 에라토스테네스의 체
def solution2(n):
    num = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in num:
            num -= set(range(i*i,n+1,i))
    return len(num)


print(solution(10))
print(solution(5))