# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(n):
    count = 0
    while n>1:
        if count >= 500:
            return -1
        else:
            if n % 2 == 0:
                n = n//2
                count += 1
            else:
                n = n*3+1
                count += 1
    return count
print(solution(16))
print(solution(1))

'''
num이 1이 될 때 까지 반복
만약 count가 500을 넘는다면 return -1
'''

# def solution(num):
#     count = 0
#     while count < num:
#         count += 1
#         print(count)
#         if count == 16:
#             print('끝')
    


# print(solution(16))
# print(solution(1))

# while 문

