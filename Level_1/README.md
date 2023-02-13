# Python 프로그래머스 Level_1
> 목차
> 1. 2016년([https://school.programmers.co.kr/learn/courses/30/lessons/12901](https://school.programmers.co.kr/learn/courses/30/lessons/12901))
> 2. 나누어 떨어지는 숫자 배열([https://school.programmers.co.kr/learn/courses/30/lessons/12910](https://school.programmers.co.kr/learn/courses/30/lessons/12910))
> 3. 문자열 내 마음대로 정하기([https://school.programmers.co.kr/learn/courses/30/lessons/12915](https://school.programmers.co.kr/learn/courses/30/lessons/12915))



<br>

## 1. 2016년

먼저 리스트에 요일을 담아주자.
입력한 날짜의 이전 날 수를 더해준 다음 7로 나누고 리스트에서 그 나머지값에 해당하는 위치에 있는 요일을 반환해주자

```sh
1. days 리스트에 요일 담기
    이 때 1월 1일이 금요일이기 때문에 첫번째 요소가 금요일이 되도록 담아주자
# days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]

2. 2016년의 매달 말일은 아래와 같다
1월 31일, 2월 29일, 3월 31일, 4월 30일, 5월 31일, 6월 30일,
7월 31일, 8월 31일, 9월 30일, 10월 31일, 11월 30일, 12월 31일
주어진 이전의 날 수를 더해줘야 하기 때문에 이 값들도 리스트에 담아주자
# month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

3. for 문으로 a-1월까지의 이전 모든 일 수를 더해주고, a월의 b일도 더해주자.
    # date = 0
    # for i in range(a-1):
    #     date += month[i]
    # date += b
3-1 for 문이 아니라 인덱스 슬라이싱으로도 구현할 수 있다
    # date = sum(month[:a-1])+b

4. date를 7로 나누고 days에서 그 값에 해당하는 위치에 있는 요일을 반환하는데 리스트는 0부터 시작하기 때문에 date%7 - 1을 하고 반환해주자
    # answer = days[date%7-1]
    # return answer
```

<br>

## 2. 나누어 떨어지는 숫자 배열
arr를 for 문 돌려서 나누어 떨어지는 수를 리스트에 담아서 리턴하기전에 정렬해주자
answer의 원소가 없다면 -1를 return 하자

```sh
1. 배열을 for문을 돌리며 divisor로 나누어 떨어지는지 확인하고 나누어 떨어진다면 answer에 담아주기
# answer=[]
# for i in arr:
#     if i % divisor == 0:
#         answer.append(i)

2. return 전에 정렬해주기
# answer.sort()

3. answer의 개수가 0이라면 -1를 담아 return 하기
# if len(answer)==0:
#     answer.append(-1)
# return answer

```

<br>

## 3. 문자열 내 마음대로 정하기

strings의 각각의 단어의 index n번째에 위치한 알파벳을 각각의 맨 앞에 붙여주고 정렬을 하자.
그리고 return할 때 두번째 알파벳부터 return해주자

```sh
1. for문으로 strings의 각각의 단어 맨 앞에 index n번째에 위치한 알파벳을 붙여서 담아주자
    # for i in strings:
    #     i = i[n]+i
    #     lst.append(i)

2. 정렬
    #lst.sort()

3. 슬라이싱을 해서 return 해주자
    # for j in lst:
    #     j = j[1:]
    #     answer.append(j)
    # return answer

```