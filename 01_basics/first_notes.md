# 아웃풋
```
# Print "Hello World!"
print("Hello, World!")
# Print "Have a good day."
print("Have a good day.")
# Print "Learning Python is fun!"
print("Learning Python is fun!")
```
### 실행 결과
```
Hello, World!
Have a good day.
Learning Python is fun!
```


# 주석처리 하기
```
# Write a single-line comment
#This is a comment
# Comment out this line so it does not run:
#print("This should not run")#
```
# Add a multiline comment
```
"""
This is a multiiline
comment
"""
```

# 변수
```
x=5
y="John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)
```
### 실행 결과
```
5
John
Sally
```

# 변수_캐스팅
```
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
```
### 실행 결과
```
3
3
3.0
```
# 변수_타입구하기
```
x=5
y="John"
print(type(x))
print(type(y))
```
### 실행 결과
```
<class 'int'>
<class 'str'>
```

# "" 와''차이
```
a = "John"
b = 'John'
print(a)
print(b)
```
### 실행 결과
```
John
John
```

# 대소문자 구분
```
a=4
A="Sally"
print(a)
print(A)
```
### 실행 결과
```
4
Sally
```
# 변수이름

```
import random
a=[1,2,3]
선택= random.choice(a)
print(선택)
```

# 반복문을 활용한 데이터 처리 기초

## 1. range()

range()는 연속된 숫자 범위를 생성하는 함수이다.

- 기본 형태: range(시작, 끝, 간격)
- 끝 값은 포함되지 않는다.

```python
nums = list(range(0, 10))
print(nums)
```

### 실행 결과
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 2. for문을 이용한 데이터 처리

리스트 데이터를 반복문으로 하나씩 꺼내 처리할 수 있다.

```python
nums = [1, 2, 3, 4, 5]

for i in nums:
    print(i)
```

### 실행 결과
```
1
2
3
4
5
```

---

## 3. 반복문 활용 예시 (합계 구하기)

반복문을 이용하면 여러 값의 합을 쉽게 구할 수 있다.

```python
nums = [1, 2, 3, 4, 5]
total = 0

for i in nums:
    total = total + i

print(total)
```

### 실행 결과
```
15
```

---

## 📌 느낀 점

- 반복문을 이용하면 여러 데이터를 효율적으로 처리할 수 있다.
- 특히 합계 계산처럼 데이터 분석의 기초 작업에 활용될 수 있다.
- 아직은 익숙하지 않지만 점점 이해하고 있다.