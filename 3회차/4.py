# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0
    while num > 1:
        if count < 500:
            if num % 2 == 0:
                num = num//2
                count = count + 1
            else:
                num = num * 3 + 1
                count = count + 1
        else:
            return -1
    return count

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
    


print(solution(16))
print(solution(1))
# while 문