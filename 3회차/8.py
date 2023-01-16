# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 내림차순
def solution1(citations):
    citations.sort() # 정렬
    count = len(citations)
    for i in range(count):
        if citations[i] >= count - i:
            return count - i
    return 0

# 오름차순
def solution(citations):
    n = len(citations) # 발표한 논문 개수 -> Max H-index
    sort_citations = sorted(citations,reverse=True)   # 논문 인용 내림순으로 정렬
    if n < sort_citations[-1] : # Max H-index의 값이 제일 적게 인용된 횟수보다 작은지 확인
        return n
    
    for h, v in enumerate(sort_citations):  # 해당 논문의 인용횟수 v, v번 이상 인용횟수 초과 인용된 논문의 갯수(h-index)를 h
        if h >= v:                          
            return h

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

