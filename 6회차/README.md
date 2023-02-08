# Python 백준 알고리즘 6회차
> 목차
> 1. 1912번 연속합([https://www.acmicpc.net/problem/1912](https://www.acmicpc.net/problem/1912))
> 2. 2579번 계단 오르기
([https://www.acmicpc.net/problem/2579](https://www.acmicpc.net/problem/2579))
> 3. 1463번 1로 만들기
([https://www.acmicpc.net/problem/1463](https://www.acmicpc.net/problem/1463))




<br>

## 1. 1912번 연속합

```sh
for 문을 돌리면서 연속된 값을 더해주며 lst에 담아서 마지막에 최대값을 출력하자


1. 첫번째 줄에 연속될 숫자의 개수를 입력받게 하고
# n = int(input())
2. 두번째 줄에 입력된 개수만큼 수열을 입력받게 하자
#a = list(map(int, input().split()))
3. for 문으로 돌리면서 연속된 수를 더해줘서 더 큰 값을 lst에 담아두자.
# for i in range(len(a)-1):
#     lst.append(max((lst[i]+a[i+1]),a[i+1]))
이때 첫번째 값 하나만이 최대값이 될 수 있기 때문에 처음부터 lst에 따로 담아두자
# lst = [a[0]]

```

<br>

## 2. 게임 맵 최단거리


```sh
최단거리를 구하는 문제이기 때문에 BFS를 사용해보자

보자마자 BFS로 풀어야겠다고 생각은 했지만 직접 작성하기가 어려웠다..
BFS의 개념은 이해했지만 직접 문제를 보고 BFS를 적용해서 코드를 작성하기엔 아직 어렵다.. 직접 코드를 짤 수 있을 때 까지 더 연습을 해야겠다

```
<br>

