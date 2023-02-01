# Python 프로그래머스/백준 알고리즘 4회차
> 목차
> 1. 타겟 넘버([https://school.programmers.co.kr/learn/courses/30/lessons/43165](https://school.programmers.co.kr/learn/courses/30/lessons/43165))
> 2. 게임 맵 최단거리 ([https://school.programmers.co.kr/learn/courses/30/lessons/1844](https://school.programmers.co.kr/learn/courses/30/lessons/1844))
> 3. 입국심사([https://school.programmers.co.kr/learn/courses/30/lessons/43238](https://school.programmers.co.kr/learn/courses/30/lessons/43238))
> 4. 공유기 설치 ([https://www.acmicpc.net/problem/2110](https://www.acmicpc.net/problem/2110))
> 5. 포도주시식 ([https://www.acmicpc.net/problem/2156](https://www.acmicpc.net/problem/2156))
> 6. 더 맵게 ([https://school.programmers.co.kr/learn/courses/30/lessons/42626](https://school.programmers.co.kr/learn/courses/30/lessons/42626))




<br>

## 1. 타겟 넘버

```sh
n개의 자연수를 더하거나 빼서 target number를 만드려고 한다.
방법의 수를 반환하는 코드를 작성하는 것

n개의 자연수에서 더하거나 빼서 만들 수 있는 모든 경우의 수 중에서 결과가 target number인 것만 세어주면 된다

# ex)solution([4, 1, 2, 1],4)
1. num_list에 각각 숫자의 양/음수 쌍으로 넣어주기
# [(4, -4), (1, -1), (2, -2), (1, -1)]
2. product로 리스트의 모든 조합 구하기
# [(4, 1, 2, 1), (4, 1, 2, -1), (4, 1, -2, 1), (4, 1, -2, -1), (4, -1, 2, 1), (4, -1, 2, -1), (4, -1, -2, 1), (4, -1, -2, -1), (-4, 1, 2, 1), (-4, 1, 2, -1), (-4, 1, -2, 1), (-4, 1, -2, -1), (-4, -1, 2, 1), (-4, -1, 2, -1), (-4, -1, -2, 1), (-4, -1, -2, -1)]
3. for 문으로 돌리면서 각각의 조합을 더해서 결과가 target number 인 것만 세어주기

```


product
```sh
product : 데카르트 곱. 두 개 이상의 리스트의 모든 조합을 구할 때 사용된다

from itertools import product

_list = ["012", "abc", "!@#"]
pd = list(product(*_list))
# [('0', 'a', '!'), ('0', 'a', '@'), ('0', 'b', '!'), ('0', 'b', '@'), ('1', 'a', '!'), ('1', 'a', '@'), ('1', 'b', '!'), ('1', 'b', '@')]

```

<br>

## 2. 게임 맵 최단거리


```sh


```
