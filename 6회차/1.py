# 1912번 연속합
# https://www.acmicpc.net/problem/1912
n = int(input())
a = list(map(int, input().split()))
lst = [a[0]]
for i in range(len(a)-1):
    lst.append(max((lst[i]+a[i+1]),a[i+1]))
print(max(lst))
