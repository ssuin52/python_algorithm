# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution1(citations):
    citations.sort()
    count = len(citations)
    for i in range(count):
        if citations[i] >= count - i:
            return count - i
    return 0

def solution2(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)
print(solution2([3,0,6,1,5]))

# item = ["First", "Second", "Third"] 
# for idx, i in enumerate(item):
# 	print(idx, i)

# citations=[3,0,6,1,5]
# citations.sort()
# print(citations)
# citations.sort(reverse=True)
# print(citations)

# for idx, citation in enumerate(citations):
	# print(idx, citation)