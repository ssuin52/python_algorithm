# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    if len(set(nums)) >= len(nums)//2:
        return len(nums)//2
    else:
        return len(set(nums))

#(1.11ms, 11MB)
def solution(nums):
    return len(nums)//2 if len(set(nums))>= len(nums)//2 else len(set(nums))

# 다른사람 풀이
def solution2(ls):
    return min(len(ls)/2, len(set(ls)))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))


# lst = [3,1,1,2,3]
# nums = list(set(lst))
# print(len(nums))