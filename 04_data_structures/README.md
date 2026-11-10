# 📚 자료구조 실습 프로젝트

## 📌 프로젝트 소개

Python을 활용하여 주요 자료구조와 탐색 알고리즘을 직접 구현한 프로젝트입니다.

배열 기반의 리스트(List), 스택(Stack), 큐(Queue), 덱(Deque), 집합(Set), 우선순위 큐(Priority Queue)를 구현하였으며, 이를 활용한 계산기, 라인 편집기, 미로 탐색 프로그램을 제작하였습니다.

자료구조의 내부 동작 원리와 알고리즘의 탐색 과정을 직접 구현하며 학습하는 것을 목표로 진행하였습니다.

---

## 🛠 개발 환경

* Python 3.14.3
* Flet
* VS Code

---

## 📂 프로젝트 구성

```text
자료구조실습
├── listADT.py
├── setADT.py
├── stackADT.py
├── queue.py
├── 선형덱.py
├── 원형덱.py
├── 우선순위큐_선형큐.py
├── stack_calculator.py
├── lineeditor_flet.py
├── maze_DFS_flet.py
├── 넓이우선탐색미로.py
└── 전략미로.py
```

---

## 🚀 주요 구현 내용

### 1. ListADT

배열 기반 리스트 구현

기능

* Insert
* Delete
* Search
* Replace
* Append
* Clear

---

### 2. SetADT

집합 자료구조 구현

기능

* 원소 삽입
* 원소 삭제
* 포함 여부 검사
* 합집합(Union)
* 교집합(Intersection)
* 차집합(Difference)
* 집합 비교

---

### 3. StackADT

LIFO(Last In First Out) 구조 구현

기능

* Push
* Pop
* Peek
* Size
* Clear

---

### 4. Queue

#### 선형 큐 (Linear Queue)

* FIFO 구조
* front와 rear를 이용한 구현

#### 원형 큐 (Circular Queue)

* 순환 구조 적용
* 공간 재사용 가능

---

### 5. Deque

#### 선형 덱

* 앞/뒤 삽입
* 앞/뒤 삭제

#### 원형 덱

* 원형 구조를 활용한 공간 효율 향상

---

### 6. Priority Queue

우선순위가 높은 데이터를 먼저 처리하는 큐 구현

예시

```python
enqueue(3)
enqueue(1)
enqueue(5)
enqueue(2)

dequeue()  # 5
dequeue()  # 3
```

---

## 🖥 응용 프로그램

### Stack Calculator

스택을 활용하여 중위 표기식 수식을 계산하는 프로그램

예시

```text
( 3 + 4 ) * 2
```

결과

```text
14
```

---

### Line Editor

리스트 자료구조를 활용한 텍스트 편집기

기능

* 행 삽입
* 행 삭제
* 행 수정
* 파일 저장
* 파일 불러오기

Flet GUI 기반으로 구현

---

### DFS Maze Search

스택을 활용한 깊이 우선 탐색(DFS)

특징

* 한 경로를 끝까지 탐색
* 막히면 되돌아가기(Backtracking)

---

### BFS Maze Search

큐를 활용한 너비 우선 탐색(BFS)

특징

* 가까운 노드부터 탐색
* 최단 경로 탐색에 활용 가능

---

### Priority Maze Search

우선순위 큐를 활용한 미로 탐색

특징

* 출구와의 거리를 계산
* 출구에 가까운 경로를 우선 탐색

---

## 📖 학습 내용

본 프로젝트를 통해 다음 내용을 학습하였습니다.

* 배열 기반 자료구조 구현
* 스택(Stack)과 큐(Queue)의 동작 원리
* 선형 구조와 원형 구조 비교
* DFS와 BFS 탐색 알고리즘
* 우선순위 큐 활용 방법
* 자료구조 기반 문제 해결 능력 향상
* Python GUI 프로그래밍(Flet)

---

## 📈 프로젝트 결과

* 주요 자료구조 직접 구현 완료
* 탐색 알고리즘 실습 완료
* GUI 응용 프로그램 개발 경험 확보
* 자료구조와 알고리즘 이해도 향상

---
한국폴리텍대학 AI 소프트웨어 과정

2026 자료구조 실습 프로젝트
