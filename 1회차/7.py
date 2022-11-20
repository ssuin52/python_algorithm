# 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = [''] * n
    # 이진수로 바꾸고 자리수 맞춰주기
    for i in range(len(arr1)):
        bin1 = bin(arr1[i])[2:].zfill(n)
        bin2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            # OR 연산 해주기
            if bin1[j] == '0' and bin2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))