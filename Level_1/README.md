# Python 프로그래머스 Level_1
> 목차
> 1. 2016년([https://school.programmers.co.kr/learn/courses/30/lessons/12901](https://school.programmers.co.kr/learn/courses/30/lessons/12901))




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

