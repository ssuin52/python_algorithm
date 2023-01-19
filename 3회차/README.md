# Python 프로그래머스 알고리즘 3회차


목차
1. 문자열 내 p와 y의 개수([https://school.programmers.co.kr/learn/courses/30/lessons/12916](https://school.programmers.co.kr/learn/courses/30/lessons/12916))
2. 핸드폰 번호 가리기([https://school.programmers.co.kr/learn/courses/30/lessons/12948](https://school.programmers.co.kr/learn/courses/30/lessons/12948))
3. 제일 작은 수 제거하기 ([https://school.programmers.co.kr/learn/courses/30/lessons/12935](https://school.programmers.co.kr/learn/courses/30/lessons/12935))
4. 콜라츠 추측([https://school.programmers.co.kr/learn/courses/30/lessons/12943](https://school.programmers.co.kr/learn/courses/30/lessons/12943))
5. 수박수박수박수박수박수?([https://school.programmers.co.kr/learn/courses/30/lessons/12922](https://school.programmers.co.kr/learn/courses/30/lessons/12922))
6. 가운데 글자 가져오기([https://school.programmers.co.kr/learn/courses/30/lessons/12903](https://school.programmers.co.kr/learn/courses/30/lessons/12903))
7. 올바른 괄호 - 스택/큐([https://school.programmers.co.kr/learn/courses/30/lessons/12909](https://school.programmers.co.kr/learn/courses/30/lessons/12909))
8. H-Index ([https://school.programmers.co.kr/learn/courses/30/lessons/42747](https://school.programmers.co.kr/learn/courses/30/lessons/42747))
9. 폰켓몬 ([https://school.programmers.co.kr/learn/courses/30/lessons/1845](https://school.programmers.co.kr/learn/courses/30/lessons/1845))
10. 다트게임 ([https://school.programmers.co.kr/learn/courses/30/lessons/17682](https://school.programmers.co.kr/learn/courses/30/lessons/17682))

<br>

## 1. 문자열 내 p와 y의 개수
```sh
1. 입력값은 대/소문자가 섞여 있으므로 소문자로 통일해주자
* lower()
2. p의 개수와 y의 개수를 비교하자
* count()
3. 일치하면 True, 일치하지 않으면 False

연산자 결과는 True, False 불린값으로 나온다!!
if 쓸필요 없음!
```

## 2. 핸드폰 번호 가리기

1. for 문 사용X
```sh
   * 입력값의 개수에서 -4 한 만큼 * 
   * 입력값의 뒤에서 4자리 더하기
```

2. for 문 사용
```sh
   * 입력값의 마지막 4자리 전까지 for 문 돌리며 * append하기
   * 입력값의 마지막 4자리 append하기
   * 공백 제외하고 return
```


<br>

## 3. 제일 작은 수 제거하기

```sh
   * arr의 개수가 1일 경우 [-1] return 
   * 1이 아닐경우 arr의 최솟값 제거 후 return arr
```


## 4. 콜라츠 추측

1. While 문 (0.13ms, 10.2MB)
```sh
   * 문제에서 주어진 대로 하나씩 따라가자! 
>    1. 입력된 수가 짝수라면 2로 나눕니다. 
>    2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
>    2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
   * count에 횟수를 카운트 해주자
   * count가 500보다 커지면 -1 return 해주자
```


2. 재귀함수(0.48ms, 10.4MB)
```sh
   * 반복되는 부분을 재귀로 표현
   * 재귀로 표현했을 때 가독성이 더 좋고, 변수사용을 줄일 수 있다
   * 하지만 성능이 더 좋진 않다
```

## 5. 수박수박수박수박수박수?

1. (0.01ms, 10.1MB)
```sh
   * n을 2로 나눈 몫 만큼 '수박'이 반복된다
   * 따라서 짝수일 때는 '수박'으로 떨어지지만
   * 홀수일 때는 마지막에 '수'가 붙는다
```

## 6. 가운데 글자 가져오기

1. (0.00ms, 10.3MB)
```sh
   * 입력값이 홀수이면 2로 나눈 가운데 값을 return
   * 입력값이 짝수이면 2로 나눈 값의 앞, 뒤값을 return
```

## 7. 올바른 괄호 - 스택/큐

1. 5,11번 에러발생
```sh
   * )로 시작하거나 (로 끝나면 false
   * 그 외에 (와 )의 개수가 일치하지 않으면 false
```

2. 정확성(0.02ms, 10.3MB) 효율성(7.50ms, 10.5MB)
```sh
   * )로 시작하면 false
   * (이면 stack에 추가
   * )이면 stack에 있는 ( pop
   * 마지막에 stack이 비어있지 않으면 false 비어있으면 true

   )가 입력될 경우 pop을 해줄때
   stack이 비어있는 경우를 처리해주지 않아서 IndexError발생
   -> 비어있을 경우 False
```


## 8. H-Index

1. 
   * n편 중 h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h번 이하인용된 경우가 h의 최댓값구하기


<br>

## 9. 폰켓몬

1. (0.74ms, 11MB)
```sh
   * 중복되지 않는 폰캣몬의 개수와 전체 폰캣몬의 개수의 절반의 수와 비교
   * 중복되지 않은 폰캣몬의 개수가 더 많다면 전체 폰캣몬 개수의 절반을 return
   * 더 적다면 중복되지 않은 폰캣몬의 개수를 return

   -> 중복되지 않은 폰캣몬은 set()을 이용
```

2. (0.76ms, 10.9MB)
```sh
   * 결국 중복되지 않은 폰캣몬의 개수와 전체 폰캣몬 개수의 절반과 비교하여 더 작은 값을 return하는 것
```

## 10. 다트게임

1. 런타임 에러
```sh
   * isnumeric()함수를 사용하여 숫자인지 문자인지 구별
   * 숫자이면 더하고
   * 문자이면 각각 상황에 맞게 연산 해준다
```

