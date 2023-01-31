# Python 프로그래머스 알고리즘 1회차
> 목차
> 1. 평균 구하기 ([https://school.programmers.co.kr/learn/courses/30/lessons/12944](https://school.programmers.co.kr/learn/courses/30/lessons/12944))
> 2. 짝수와 홀수([https://school.programmers.co.kr/learn/courses/30/lessons/12937](https://school.programmers.co.kr/learn/courses/30/lessons/12937))
> 3. 자릿수 더하기([https://school.programmers.co.kr/learn/courses/30/lessons/12931](https://school.programmers.co.kr/learn/courses/30/lessons/12931))
> 4. 자연수 뒤집어 배열로 만들기([https://school.programmers.co.kr/learn/courses/30/lessons/12932](https://school.programmers.co.kr/learn/courses/30/lessons/12932))
> 5. 숫자 문자열과 영단어([https://school.programmers.co.kr/learn/courses/30/lessons/81301](https://school.programmers.co.kr/learn/courses/30/lessons/81301))
> 6. 체육복 ([https://school.programmers.co.kr/learn/courses/30/lessons/42862](https://school.programmers.co.kr/learn/courses/30/lessons/42862))
> 7. 비밀지도 ([https://school.programmers.co.kr/learn/courses/30/lessons/17681](https://school.programmers.co.kr/learn/courses/30/lessons/17681))
> 8. 약수의 개수와 덧셈 ([https://school.programmers.co.kr/learn/courses/30/lessons/77884](https://school.programmers.co.kr/learn/courses/30/lessons/77884))
> 9. 없는 숫자 더하기 ([https://school.programmers.co.kr/learn/courses/30/lessons/86051](https://school.programmers.co.kr/learn/courses/30/lessons/86051))
> 10. 완주하지 못한 선수 ([https://school.programmers.co.kr/learn/courses/30/lessons/42576](https://school.programmers.co.kr/learn/courses/30/lessons/42576))

<br>

## 3. 자릿수 더하기
for문
```sh
3-1 
자연수를 string으로 바꿔서 한글자씩 for문을 돌려 더해주는데 더해줄 때는 다시 int로 바꿔서 더해준다
```

while문
```sh
3-2
입력값 n을 받아서
while문으로 10을 나눠주는것을 반복하는데
나머지는 answer에 담아주고 
몫은 다시 n에 담아준다.
n이 10보다 작아지는 순간 answer+n 을 반환한다
```

## 4. 자연수 뒤집어 배열로 만들기
```sh
str으로 바꿔서 한글자씩 append해주고 reverse로 역순 취해주기
```

## 5. 숫자 문자열과 영단어
```sh
if, elif 사용해서 replace로 문자를 바꿔줬더니
1개의 문자열만 숫자로 바뀌고 나머지는 안바뀌길래
lst로 바꿔줘야하는 문자열을 담아주고 for문으로 돌려줬다
```

## 6. 체육복
```sh
여분의 체육복을 가진 학생중 체육복을 잃어버린 학생을 제외하고
체육복을 잃어버린 학생 중 여분의 체육복이 있는 학생을 제외시켜준다

체육복을 잃어버린 학생을 a라고 할 때 여분의 체육복을 갖고 있는 학생 중 a-1, a+1이 있으면 빌릴 수 있기 때문에 lost_st에서 a를 제외시켜주고

결과적으로 전체 학생수에서 남은 lost_st를 빼준다

첫번째 풀이
정렬이 필요한 이유
n=5 reserve=[1, 3] lost=[2,4] 일 때
1번이 2번에게 빌려주고, 3번이 4번에게 빌려줄 수 있지만

n=5 reserve=[3, 1] lost=[2,4] 일 면
3번이 2번에게 빌려주고 4번은 체육복을 빌릴 수 없게된다.

때문에 최댓값을 반환하는 문제이므로 정렬이 필요하다
(처음에 정렬을 안했다가 오류)
```

## 7. 비밀지도
```sh
이진수로 바꿔주고 자리수를 맞춰준 다음
or 연산을 해주자
```

## 8. 약수의 개수와 덧셈 

약수의 개수를 구하는 코드를 짜서 for문으로 left부터 right까지 약수의 개수를 구하고 그 때마다 홀/짝 판별을 해주자

```sh
먼저 약수의 개수를 구하는 코드부터 작성했다.
만약 n의 약수의 개수를 구한다고 했을 때는
for문으로 1부터 n까지(range(1,n+1)) n을 나눴을 때 
나머지가 0이 되면 lst에 넣어주고
len(lst)를 하면 약수의 개수를 알 수 있다

이제 n의 약수의 개수가 아니라 left부터 right까지의 약수의 개수를 구해야하므로 for문을 또 돌려주자
for 문이 돌 때 홀/짝 판별을 해줘서 짝수이면 더해주고 홀수이면 빼주자
```

## 9. 없는 숫자 더하기
```sh
리스트끼리 뺄셈은 안된다..
리스트 차집합 구글링해보니 set은 뺄셈이 된다더라
set으로 바꿔서 빼주면 진짜 간단한데 
뭔가 다른방법으로도 풀고 싶어서 보니까 
listA-listB 를 할 때 for문으로 listA 안에 있는 원소 중에서 listB에 없는 원소만 뽑아주는 방법이 있더라
이 방법으로 해봤다
```



