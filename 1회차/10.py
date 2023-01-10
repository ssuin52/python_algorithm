# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# #1.딕셔너리를 활용 - 런타임에러
def solution(participant, completion):
    temp = {}
    for i in participant:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    for i in completion:
        if i in temp:
            del temp[i]
        else:
            temp[i] -= 1
    return list(temp.keys())[0]



# #2. collections.Counter
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 정확성(0.6ms, 10.4mb)
# 효율성(78.20ms, 39.mb)
print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))



#3. hash()활용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

# 정확성(0.87ms, 10.4mb)
# 효율성(53.51ms, 37.7mb)

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
a = 'a'
b = 'b'
c = 'c'
d = 'a'

print(hash(a))
print(hash(b))
print(hash(c))
print(hash(d))




# def solution(participant, completion):
#     completion.sort()
#     participant.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
    
#     return  participant[-1]

