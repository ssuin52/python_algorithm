# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 문제 설명

# 네오와 프로도가 숫자놀이를 하고 있습니다. 
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

# 제한사항
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

def solution1(s):
    s = str(s)
    lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in lst:
        if 'zero' in s:
            s = s.replace('zero','0')
        elif 'one' in s:
            s = s.replace('one','1')
        elif 'two' in s:
            s = s.replace('two','2')
        elif 'three' in s:
            s = s.replace('three','3')
        elif 'four' in s:
            s = s.replace('four','4')
        elif 'five' in s:
            s = s.replace('five','5')
        elif 'six' in s:
            s = s.replace('six','6')
        elif 'seven' in s:
            s = s.replace('seven','7')
        elif 'eight' in s:
            s = s.replace('eight','8')
        elif 'nine' in s:
            s = s.replace('nine','9')
    answer = int(s)
    return answer


# 0.04ms
# 10.5mb
print(solution1("23four5six7"))
print(solution1("2three45sixseven"))
print(solution1("one4seveneight"))
print(solution1("123"))



def solution2(s):
    answer = 0
    lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in lst:
        s = s.replace(i, str(lst.index(i)))
    answer = int(s)
    return answer

# 0.02ms
# 10.5mb
#     
print(solution2("23four5six7"))
print(solution2("2three45sixseven"))
print(solution2("one4seveneight"))
print(solution2("123"))
