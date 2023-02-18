# Python 프로그래머스 Level_1
> 목차
> 1. 2016년([https://school.programmers.co.kr/learn/courses/30/lessons/12901](https://school.programmers.co.kr/learn/courses/30/lessons/12901))
> 2. 나누어 떨어지는 숫자 배열([https://school.programmers.co.kr/learn/courses/30/lessons/12910](https://school.programmers.co.kr/learn/courses/30/lessons/12910))
> 3. 문자열 내 마음대로 정하기([https://school.programmers.co.kr/learn/courses/30/lessons/12915](https://school.programmers.co.kr/learn/courses/30/lessons/12915))
> 4. 신규 아이디 추천([https://school.programmers.co.kr/learn/courses/30/lessons/72410](https://school.programmers.co.kr/learn/courses/30/lessons/72410))
> 5. 키패드 누르기([https://school.programmers.co.kr/learn/courses/30/lessons/67256](https://school.programmers.co.kr/learn/courses/30/lessons/67256))

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

<br>

## 4. 신규 아이디 추천

문제에서 주어진 규칙을 잘 따라가서 코드를 작성해보자

### 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
```sh
new_id = new_id.lower()
```
### 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
```sh
for i in new_id:
    if i.islower() or i.isdigit() or i == '-' or i =='_' or i == '.':
        answer += i
```
```sh
정규식을 사용할 수도 있다!
answer = re.sub('[^a-z0-9\-_.]', '', answer)
```

### 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
```sh
3단계 마침표가 2번 이상 연속된 부분을 하나의 마침표로 바꿀 때 
for 문을 돌려서 연속되게 나올 경우 하나를 제거해주려고 했는데
마침표가 마지막에 있을 경우 오류가 나더라
    # for j in range(len(new2)):
    #     if new2[j]=='.' and new2[j+1]=='.':
    #         new3 += ''
    #     else:
    #         new3 += new2[j]

#     Traceback (most recent call last):
#   File "Level_1/4.py", line 23, in <module>
#     print(solution('...!@BaT#*..y.abcdefghijklm.'))
#   File "Level_1/4.py", line 13, in solution
#     if new2[j]=='.' and new2[j+1]=='.':
# IndexError: string index out of range

그래서 문제에서 나오다시피 ..을 .로 치환해줬다.
    # while '..' in answer:
    #     answer = answer.replace('..', '.')

```
### 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
```sh
처음이나 끝이 마침표이면 슬라이싱 해주는거로 간단하게 생각했다가 오류가나서 고생했다.

첫 글자가 마침표이고 만약 글자수가 1이면 마침표를 반환해주자

    # if answer[0]=='.':
    #     if len(answer) > 1:
    #         answer = answer[1:]
    #     else:
    #         answer == '.'
    # if answer[-1]=='.':
    #     answer = answer[:-1]
```
### 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
```sh
if len(answer)==0:
    answer = 'a'
```
### 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
```sh
if len(answer) > 15:
    answer = answer[:15]
    if answer[-1]=='.':
        answer = answer[:-1]
```
### 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
```sh
while len(answer) < 3:
    answer += answer[-1]  
```


<br>

## 5. 키패드 누르기

1,4,7은 L(왼손), 3,6,9는 R(오른손), 
2,5,8,0은 더 가까이 있는 손(위치가 같을 경우에는 hand인 손)

<br>

1,4,7은 왼손에 3,6,9는 오른손에 담고 나머지 숫자를 처리하기 위해 왼쪽손의 위치와 오른쪽 손의 위치를 저장하기위해 stack에 따로 담아주고 
pop으로 비교해주려고 했는데 비교를 못하겠어서...ㅠㅠ 아이디어가 생각이 나질 않았다.

<br>

거리 비교를 어떻게 하나 봤더니 좌표를 이용할 수 있더라. 해보자


### 1. 키패드를 좌표로 위치를 정하자
```sh
    # pad = {'1':(0,0), '2':(0,1), '3':(0,2),
    #        '4':(1,0), '5':(1,1), '6':(1,2),
    #        '7':(2,0), '8':(2,1), '9':(2,2),
    #        '*':(3,0), '0':(3,1), '#':(3,2)
    #     }
```

### 2. 처음 왼손,오른손 위치를 정해주자
```sh
    # left_pad = pad['*']   #처음 왼손의 위치
    # right_pad = pad['#']  #처음 오른손의 위치
```

### 3. for문으로 입력값을 돌면서 각각의 경우에 맞게 answer를 추가하자

#### 3-1. 무조건 왼손으로 입력해야 하는 경우 (1, 4, 7)
```sh
        if number in [1,4,7]:
            answer += 'L' # L을 추가하고 
            left_pad = pad[str(number)] # 왼손 위치를 업데이트 해주자
```
#### 3-2. 무조건 오른손으로 입력해야 하는 경우 (3, 6, 9)
```sh
        elif number in [3,6,9]: 
            answer += 'R' # R을 추가하고
            right_pad = pad[str(number)] # 오른손 위치를 업데이트 해주자
```
#### 3-3. (2, 5, 8, 0)인 경우 거리를 계산하여 비교해주자
```sh
        else:
            # 1. 거리 제곱의 합 이용
            left_d = math.ceil(math.sqrt(math.pow((pad[str(number)][0]-left_pad[0]),2)+math.pow((pad[str(number)][1]-left_pad[1]),2))))
            right_d = math.ceil(math.sqrt(math.pow((pad[str(number)][0]-right_pad[0]),2)+math.pow((pad[str(number)][1]-right_pad[1]),2))))

            # 2. 절댓값 이용
            left_d = abs(left_pad[0] - pad[str(number)][0]) + abs(left_pad[1] - pad[str(number)][1])
            right_d = abs(right_pad[0] - pad[str(number)][0]) + abs(right_pad[1] - pad[str(number)][1])
```
##### 3-3-1. 거리비교 했을 시 처리(같을 경우 hand 선택)
```sh
                if left_d < right_d:
                    answer += 'L'
                    left_pad = pad[str(number)]
                elif left_d > right_d:
                    answer += 'R'
                    right_pad = pad[str(number)]
                else:
                    if hand == 'left':
                        answer += 'L'
                        left_pad = pad[str(number)]
                    else:
                        answer += 'R'
                        right_pad = pad[str(number)]

```
<br>
3-3에서 거리제곱의 합을 이용하여 구할 때 math.ceil(올림)을 안할 경우 일부 오류
<br>
왜?????????????