#최소 직사각형
#https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    w = []
    h = []
    for x, y in sizes:
        if x >= y:
            w.append(x)
            h.append(y)
        else:
            h.append(x)
            w.append(y)
    answer = max(w) * max(h)
    return answer

def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution2([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution2([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution2([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# result = [max(x) for x in sizes]
# print(result)