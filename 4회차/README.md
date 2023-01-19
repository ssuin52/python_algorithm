# Python 프로그래머스 알고리즘 4회차
> 목차
> 1. dfs ([https://sizzang97.tistory.com/414](https://sizzang97.tistory.com/414))
> 2. bfs ([https://sizzang97.tistory.com/414](https://sizzang97.tistory.com/414))
> 3. 최소 직사각형 ([https://school.programmers.co.kr/learn/courses/30/lessons/86491](https://school.programmers.co.kr/learn/courses/30/lessons/86491))
> 4. 모의고사([https://school.programmers.co.kr/learn/courses/30/lessons/42840](https://school.programmers.co.kr/learn/courses/30/lessons/42840))
> 5. 소수찾기([https://school.programmers.co.kr/learn/courses/30/lessons/12921](https://school.programmers.co.kr/learn/courses/30/lessons/12921))
> 6. 카펫([https://school.programmers.co.kr/learn/courses/30/lessons/42842](https://school.programmers.co.kr/learn/courses/30/lessons/42842))
> 7. 타겟 넘버([https://school.programmers.co.kr/learn/courses/30/lessons/43165](https://school.programmers.co.kr/learn/courses/30/lessons/43165))
> 8. 게임 맵 최단거리 ([https://school.programmers.co.kr/learn/courses/30/lessons/1844](https://school.programmers.co.kr/learn/courses/30/lessons/1844))


<br>

## 1. dfs(깊이 우선 탐색)

재귀로 구현
   


<br>

## 2. bfs(너비 우선 탐색)

queue로 구현


<br>

## 3. 최소 직사각형
solution1 for문 사용(1.48ms, 11.6MB)

```sh
입력되는 직사각형들의 크기를 포함하는 가장 작은 직사각형의 넓이를 return하는 문제
먼저 직사각형의 넓이는 가로,세로가 바뀌어도 같기 때문에 일관성있게 정렬을 해주자.
1. 들어오는 값 중에 어느 값이 가로, 세로를 정할 수 없기 때문에 큰 값을 가로, 작은 값을 세로로 정하고 리스트에 각각 담아주자.
2. 가로, 세로에서 각각 max 값을 구해서 곱한 값을 return 하자

w : 가로의 길이를 담을 리스트
h : 세로의 길이를 담을 리스트

for 문으로 sizes를 돌면서
값을 비교하여 큰 값은 w에 작은 값은 y에 append 한다.

그리고 answer에 max(w) * max(h)를 담아서 return 하자

```


solution2 축약식 (2.90ms, 11.3MB) # 다른사람코드

```sh
축약식으로 구현
진짜 간단하다.... 
sizes를 for 문 돌면서 큰 값(max(x)) 중 max와 작은 값(min(x)) 중 max를 곱한 값 return 하기

```


solution3 sort 사용 (3.98ms, 11.4MB) # 다른사람코드

```sh
solution1과 큰 흐름은 동일하지만 정렬을 해주는 과정에서
if 문으로 각각 x, y 값을 비교하여 담아주지 않고
sort로 정렬하여 index 0번째 값을 w에, 1번째 값을 h에 담았다.

```

<br>

## 4. 모의고사

solution1 for문 사용(2.36ms, 10.4MB)

```sh
학생 1, 2, 3 이 찍는 패턴이 있으니
정답을 입력했을 때 for 문을 돌려서 일치하는 개수를 각각 세어주자

학생 1, 2, 3의 정답 패턴을 list에 담자
각각의 학생이 맞춘 정답의 수를 담을 correct를 만들자

for문으로 돌려주면서 비교
   학생 1은 5개의 숫자가 반복되므로 5로 나눈 나머지인 인덱스와 비교
   학생 2, 3은 각각 8개 10개이므로 8, 10으로 나눈 나머지인 인덱스와 비교

일치하면 correct + 1

correct.index(max(correct))+1로 최댓값의 인덱스에 1를 더해서 
답을 구하려고 했는데 배열로 반환되는 것이 아니라 값으로 반환이 되어 오답처리가 되었다

그래서 배열로 return하기 위해 answer=[]를 만들고
거기에 최댓값의 인덱스에 1을 더하여 append한 값을 return 했다.

```

<br>

## 5. 소수찾기

solution 이중 for문
정확성 테스트(2989.78ms, 10.4MB)
효율성 테스트(3212.31ms, 10.5MB)

```sh
1과 입력받은 n 사이에 있는 소수의 개수를 반환해야 한다

a가 소수인지 판별하기 위해서는
2부터 a의 제곱근까지 차례대로 a를 나눴을 때 나누어 떨어지지 않는다면 소수이다.
때문에 나누어 떨어지지 않을 경우 count를 세어주는데

1부터 n까지의 소수의 개수를 구해야 하므로
1은 소수가 아니므로 range로 2부터 n+1까지 for 문을 돌리자


``` 

solution2 에라토스테네스의 체
정확성 테스트 (229.72ms, 113MB)
효율성 테스트 (255.50ms, 116MB)

```sh
첫번째 방법이 이중 for문을 사용하여 성능이 너무 안좋다
다른 사람 풀이를 보던 중 성능이 좋아보이는 방법이 보였다
우와 효율성이 훨 좋다

에라토스테네스의 체를 이용한 방법이다

1은 소수가 아니므로 2부터 n까지를 set에 담는다(뺄셈할거라)
n의 최대 약수는 루트n 이하이므로
for i in range(2, int(n**0.5)+1):
만약 i가 num 안에 있으면 
set에 i*i에서 n까지 i의 간격으로 담고
num에서 set을 뺀다 # i*i인 이유는 i는 빼면 안되니까!

len(num)을 return 한다

``` 

<br>

## 6. 카펫

```sh
yellow의 가로를 x, 세로를 y라고 하면
전체 가로의 길이는 x+2, 세로는 y+2 를 구하면 된다.

1. yellow의 가로 세로 쌍을 구해서

2. brown = x*2 + y*2 +4 와 일치하는지 확인

3. 일치한다면 answer에 append

yellow의 가로 세로 쌍을 구하기 위해 for 문을 돌리자
i로 나누어 떨어진다면
먼저 나눴기 때문에 몫이 더 클 것이다
가로가 세로보다 크거나 같다고 했기 때문에 
가로에 몫을 두고(int(yellow/i)) 세로에 나눈 값을 주자

그리고 만약 brown = x*2 + y*2 +4 와 일치하면
x+2, y+2를 answer에 append해서 return 하자

``` 


<br>

## 7. 타겟 넘버

1. 
   * 

<br>

## 8. 게임 맵 최단거리
