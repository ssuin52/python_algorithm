# 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = [''] * n
    # 이진수로 바꾸고 자리수 맞춰주기
    for i in range(n):
        bin1 = bin(arr1[i])[2:].zfill(n)
        bin2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            # OR 연산 해주기
            if bin1[j] == '0' and bin2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
    return answer

# 0.05ms
# 10.2mb


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

'''
이진법 5자리수로 표현하기

1) bin 사용
print(bin(2))
# 0b10
 
2) 슬라이싱으로 0b 제거
print(bin(2)[2:])
#10
 
3) zfill로 자리수 채우기
print(bin(2)[2:].zfill(5))
#00010
'''